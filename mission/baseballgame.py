strike = 0
ball = 0

import random as rd

guard = []
for _ in range(3):
    guard.append(rd.randint(0,9))
print (guard)
                 

while strike < 3:
    
    strike = 0
    ball = 0
    
    bat = []
    for i in range(3):
        bat.append(int(input('숫자입력')))
        
    if guard[0] ==bat[0]:
        strike += 1
    elif guard[0] ==bat[1]:
        ball += 1
    elif guard[0] ==bat[2]:
        ball += 1
    
    if guard[1] ==bat[1]: 
        strike += 1
    elif guard[1] ==bat[0]:
        ball += 1
    elif guard[1] ==bat[2]:
        ball += 1
        
    if guard[2] ==bat[2]:
        strike += 1
    elif guard[2] ==bat[1]:
        ball += 1
    elif guard[2] ==bat[0]:
        ball += 1
    print (bat)    
    print (strike,"strike",ball,"ball")

print ("삼진 아웃~")