from collections import deque

def solution(numbers, target):
    answer = 0
    
    # binary tree
    q = deque()
    q.append([+numbers[0], 0])
    q.append([-numbers[0], 0])
    
    while q:
        num, index = q.popleft()
        if index < len(numbers) -1:
            q.append([num + numbers[index+1], index+1])
            q.append([num - numbers[index+1], index+1])
        else:
            if num == target:
                answer += 1
            
    return answer