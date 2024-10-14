from collections import deque

def solution(begin, target, words):
    
    if not target in words:
        return 0
    
    answer = 0
    v = [0] * len(words)
    q = deque()
    q.append([begin, 0])

    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            tmp_cnt = 0
            if not v[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp_cnt += 1
                if tmp_cnt == 1:
                    q.append([words[i], cnt+1])
                    v[i] = 1
                        
    return answer
