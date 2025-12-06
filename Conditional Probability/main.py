def a_and_b(a,b):
    prob_student=0.3
    if b==1:
        prob_dining=0.75
    else:
        prob_dining=0.25
    print(f'probability of a given b:{prob_dining}')

    if a==2:
        prob_student=0.7
        if b==1: 
            prob_dining=0.6
        else:
            prob_dining=0.4
        print(f'probability of a given b: {prob_dining}')
    prob_a_and_b=prob_dining*prob_student
    return round(prob_a_and_b,3)

print('check the probability of any event occuring.\nselect choiches: ')
print('is the student a freshmen?(1 for yes, 2 for no)')
a=int(input('enter choice for a: '))
print('is the student dining in the cafeteria? (1 for yes, 3 for no)')
b=int(input('Enter choice for b: '))
result=a_and_b(a,b)
print(f'the probability of both events occuring is: {result}')