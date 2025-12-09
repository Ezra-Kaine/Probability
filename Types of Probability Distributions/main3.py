import scipy.stats as stats
prob1=1-stats.poisson.cdf(20,15)
print(f'the probability of getting 20 or more calls in an hour is: {prob1}')
prob2=stats.poisson.cdf(21,15)-stats.poisson.cdf(16,15)
print(f'prob of getting between 17 and 21 calls in an hour is: {prob2}')