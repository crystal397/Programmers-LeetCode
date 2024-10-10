def solution(answers):
    answer = []
    a = []
    mul = len(answers) // 5 + 1
    s1 = [1,2,3,4,5] * mul
    count1 = 0
    s2 = [2,1,2,3,2,4,2,5] * mul
    count2 = 0
    s3 = [3,3,1,1,2,2,4,4,5,5] * mul
    count3 = 0
    
    for idx, val in enumerate(answers):
        if s1[idx] == val:
            count1 += 1
        if s2[idx] == val:
            count2 += 1
        if s3[idx] == val:
            count3 += 1
    answer.extend([count1, count2, count3])
    m = max(count1, count2, count3)
    answer = [index + 1 for index, val in enumerate(answer) if val == m]
    
    return answer