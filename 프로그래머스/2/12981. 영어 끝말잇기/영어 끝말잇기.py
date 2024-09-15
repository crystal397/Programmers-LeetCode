def solution(n, words):
    answer = []

    for i, p in enumerate(words):
        if i == 0:
            answer.append(p)
        else:
            if words[i-1][-1] == p[0] and p not in answer:
                answer.append(p)
                print(answer)
            else:
                if (i+1)%n == 0:
                    num = n
                else:
                    num = (i+1)%n
                return [num, (i//n)+1]
    
    return [0,0]