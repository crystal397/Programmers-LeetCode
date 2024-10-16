from heapq import heappush, heappop, heapify

def solution(operations):
    heap = []
    for op in operations:
        if op[0] == "I":
            heappush(heap, int(op[2:]))
        elif op == "D -1" and heap:
            heappop(heap)
        elif op == "D 1" and heap:
            heap = list(heap)
            heap.remove(max(heap))
            heapify(heap)
                     
    if not heap:
        return [0, 0]
    return [max(heap), min(heap)]