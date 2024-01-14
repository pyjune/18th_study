import sys
from collections import deque
# input = sys.stdin.readline
# 1번 -> 앞블럭을 뒤로, 2번 -> 뒷블럭을 앞으로, 3번 -> 두 개 선로 이어붙이기

N, M, Q = map(int, input().split())
tracks = [deque() for _ in range(M)]

idx = 1
for i in range(M):
    for j in range(N//M):
        tracks[i].append(idx)
        idx += 1
# print(tracks)
for _ in range(Q):
    p, *num = map(int, input().split())
    if p == 1:
        if tracks[num[0]]:
            tracks[num[0]].append(tracks[num[0]].popleft())
    elif p == 2:
        if tracks[num[0]]:
            tracks[num[0]].appendleft(tracks[num[0]].pop())
    else:
        a, b = num[0], num[1]
        while tracks[a]:
            tracks[b].appendleft(tracks[a].pop())
    
for t in tracks:
    if t:
        print(*t)
    else:
        print(-1)