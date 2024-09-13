def solution(n, arr1, arr2):
    answer = [0]*n
    dic = {
        '0':" ",
        '1':"#"
    }
    
    for i in range(n):
        if len(bin(arr1[i] | arr2[i])[2:]) != n:
            a = n - len(bin(arr1[i] | arr2[i])[2:])
            answer[i] = "0"*a + bin(arr1[i] | arr2[i])[2:]
        else:    
            answer[i] = bin(arr1[i] | arr2[i])[2:]
    
    for key, value in dic.items():
        for i in range(n):
            answer[i] = answer[i].replace(key, value)
    
    return answer