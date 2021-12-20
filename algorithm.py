import sys; input=sys.stdin.readline;from collections import deque
d = [[-1,0], [0,-1], [1,0], [0,1]]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    room = [list(input().strip()) for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                sy, sx = i, j
                room[i][j] = '.'
            elif room[i][j] == '*':
                room[i][j] = 1 << cnt
                cnt += 1
            
    q = deque()
    q.append([sy, sx, 0, 0])
    end = (1 << cnt) - 1
    
    visited = set()
    ans = -1
    while q:
        y, x, count, bitmask = q.popleft()
        
        if bitmask == end:
            ans = count
            break
        
        for dy, dx in d:
            ty = y + dy
            tx = x + dx
            
            if 0 <= ty < h and 0 <= tx < w and room[ty][tx] != 'x':
                if (ty, tx, bitmask) in visited:
                    continue
                
                visited.add((ty,tx,bitmask))
                
                if room[ty][tx] == '.':
                    q.append([ty, tx, count+1, bitmask])
                else:
                    q.append([ty,tx,count+1, bitmask|room[ty][tx]])
                    
    print(ans)