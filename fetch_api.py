#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import random

def fetch():
    response = requests.get("https://24zl01u3ff.execute-api.us-west-1.amazonaws.com/beta")
    object = response.json()
    flips = object['body']
    mylist = []
    for i in flips:
        if i == '0' or i == '1':
            mylist.append(int(i))
    return mylist

def EM():
    flips_30 = []

    for i in range(1,30):
         flip = fetch()
         flips_30.append(sum(flip))
    
    #assume A has a smaller probability than B
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    theta_A = min(a, b)
    theta_B = max(a, b)
    d_A = 1
    d_B = 1
    while d_A > 0.00001 or d_B > 0.00001:
        A_H = 0
        A_T = 0
        B_H = 0
        B_T = 0
        
        for h in flips_30:
            prob_A = pow(theta_A, h) * pow(1 - theta_A, 20 - h)
            prob_B = pow(theta_B, h) * pow(1 - theta_B, 20 - h)
            E_A = prob_A/(prob_A + prob_B)
            E_B = prob_B/(prob_A + prob_B)
            A_H = A_H + E_A * h
            A_T = A_T + E_A * (20 - h)
            B_H = B_H + E_B * h
            B_T = B_T + E_B * (20 - h)
        
        new_theta_A = A_H/(A_H + A_T)
        new_theta_B = B_H/(B_H + B_T)
        d_A = abs(new_theta_A - theta_A)
        d_B = abs(new_theta_B - theta_B)
        theta_A = new_theta_A
        theta_B = new_theta_B
    
    return theta_A, theta_B

[theta_A, theta_B] = EM()
print(theta_A)
print(theta_B)
