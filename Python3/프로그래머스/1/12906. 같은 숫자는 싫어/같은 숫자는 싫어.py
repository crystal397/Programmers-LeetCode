# Stack의 개념을 활용하여
# push의 개념을 append로
# top 개념을 인덱스의 [-1]로 이용하여 문제를 풀었습니다.

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif answer[-1] != arr[i]:
            answer.append(arr[i])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer
