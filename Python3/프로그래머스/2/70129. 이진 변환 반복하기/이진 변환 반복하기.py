def solution(s):
    answer = [0, 0]
    
    while s != "1":
        # 제거할 0의 개수
        answer[1] += s.count("0")

        # 0 제거 후 길이를 이진 변환
        s = format(s.count("1"), 'b')
        answer[0] += 1
    
    return answer