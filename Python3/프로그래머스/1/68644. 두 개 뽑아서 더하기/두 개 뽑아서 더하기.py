def solution(numbers):
    answer = []
    l = len(numbers)
    for i in range(l):
        for j in range(i+1, l):
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer