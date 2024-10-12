def solution(n, wires):
    answer = n
    for some in (wires[:i] + wires[i+1:] for i in range(len(wires))):
        sets = set(some[0])
        [sets.update(s) for _ in some for s in some if set(s) & sets]
        answer = min(answer, abs(len(sets) - (n - len(sets))))
    return answer