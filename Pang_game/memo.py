
lst = ["가","나","다"]

for lit_idx, lst_val in enumerate(lst):
    print(lit_idx, lst_val)


balls = [1,2,3,4]
weapons = [11,22,3,44]

for ball_inx, ball_val in enumerate(balls):
    print("ball: ",ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapos : ",weapon_val)
        if ball_val == weapon_val:
            print ("ball and weapon has crushed")
            break
    #for문에 대한 값이 끝나거나 종료가 되면 continue로 바깥으로 빠져나옴 (안에 break 조건에 대해 실행)
    else :
        continue
    print("activated outside break")
    break