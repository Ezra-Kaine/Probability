import scipy.stats as stats
prob1=stats.poisson.pmf(6,10)
print(f'probability of it raining 6 days in a month is: {prob1}')

prob2=stats.poisson.pmf(12,10)+stats.poisson.pmf(13,10)+stats.poisson.pmf(14,10)
print(f'probabolity of raining 12-14 days in a month is: {prob2}')