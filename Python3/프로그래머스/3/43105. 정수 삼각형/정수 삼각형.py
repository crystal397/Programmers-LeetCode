def solution(triangle):
    idx = len(triangle) - 1
    
    while idx:
        for i in range(idx):
            triangle[idx-1][i] += max(triangle[idx][i], triangle[idx][i+1])
        idx -= 1
     
    return triangle[0][0]