def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    left = 0
    if len(people) == 1:
        return 1
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            answer += 1
            left += 1
    return answer