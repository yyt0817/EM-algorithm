# EM-algorithm

`Result analysis`:
Even though theta_A and theta_B can converge to a specific number in each trail, their values vary between trails. In general, theta_A is around 0.3 and the theta_B is around 0.7. However, theta_A can sometimes be 0.2 and theta_B be 0.8. I think it is because we only have a set of 30 coin flip draws. I try to increase to 100 flip draws and the theta_A and theta_B is more consistent with theta_A being 0.3 and theta_B being 0.7.
`A brief explanation to my code`:
My code consists of two parts. The first part is to get a list of 20 “coin flips” by calling function fetch. After fetching the “body” of the json, I do the data preprocessing that removes additional elements (“,”, “[“, and “]”) from the body so that the function can return a list consisting of purely 0s and 1s.
The second part of my code is to estimate the probability of heads for two coins using the EM algorithm. 
