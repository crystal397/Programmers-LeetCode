def solution(absolutes, signs):
    answer = 0
    
    for i, s in enumerate(signs):
        if s == True:
            answer += absolutes[i]
            print(answer)
        else:
            answer -= absolutes[i]
            print(answer)
        
    return answer