import random
def pick_ball_experiment():
    balls=['red','blue','green','yellow','black']
    result=random.choice(balls)
    prob=balls.count('red')/len(balls)
    print(f'probability of pivking a red ball is: {prob}')

    if result=='red':
        print('youve picked a red ball')
    else:
        print(f'youve picked a {result} ball')
res=pick_ball_experiment()
print