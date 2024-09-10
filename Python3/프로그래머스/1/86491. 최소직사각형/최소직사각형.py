from collections import deque

def solution(sizes):
    answer = 0
    sizes.sort(reverse=True)
    q = deque(i for i in sizes)
    mw, mh = q.popleft()
    
    if len(sizes) == 1:
        return mw * mh
    
    while q:
        w, h = q.popleft()
        if mw < h and mh < w:
            mw = w
            mh = h
        elif mh < h: 
            if mw >= h and mh >= w:
                continue
            elif w > h:
                mh = h
            elif mw >= h and mh < w: 
                mh = w
            elif mw < h and mh > w:
                mw = h

    answer = mw * mh
    
    return answer