from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    
    while q:
        remain = weight - q.popleft()
        answer += 1
        bridge_length -= 1
        if remain >= q[0] and bridge_length > 0 and q is not empty:
            remain = weight - q.popleft()
            answer += 1
            bridge_length -= 1
        else:
            answer += 1

    return answer