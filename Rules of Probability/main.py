def Prob_a_or_b(a,b,all_posible_outcomes):
    Prob_a=len(a)/len(all_posible_outcomes)
    Prob_b=len(b)/len(all_posible_outcomes)
    Prob_a_and_b=len(a.intersection(b))/len(all_posible_outcomes)

    return Prob_a+Prob_b-Prob_a_and_b

even={2,4,6}
greater_than_2={3,4,5,6}
all_outcomes={1,2,3,4,5,6}
print(f'probability of even or greater than 2: {Prob_a_or_b(even,greater_than_2,all_outcomes)}')