def prob_six_every_time(n_rolls):
    return (1/6) ** n_rolls

n = 10
prob = prob_six_every_time(n)
print(f"Probability of rolling a 6 {n} times in a row: {prob:.6f}")
