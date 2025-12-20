def probability_white_given_white():
    total_balls = 10
    white_balls = 3

    prob_first_white = white_balls / total_balls
    prob_second_white = white_balls / total_balls  # replacement

    print(f'Probability that first ball is white: {prob_first_white}')
    print(f'Probability that second ball is white given first was white: {prob_second_white}')

    return round(prob_second_white, 3)

result = probability_white_given_white()
print(f'The required probability is: {result}')
