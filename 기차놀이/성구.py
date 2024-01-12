import sys
from collections import deque
input = sys.stdin.readline

def solution():
    lines = []
    start = 1
    for _ in range(M):
        lines.append(deque([i for i in range(start, start+N//M)]))
        start += N//M
    for q in range(Q):
        order, *line = map(int, input().split())
        if order == 1:
            target = line[0]
            if lines[target]:
                s = lines[target].popleft()
                lines[target].append(s)
        elif order == 2:
            target = line[0]
            if lines[target]:
                e = lines[target].pop()
                lines[target].appendleft(e)
        else:
            a= line[0]
            b= line[1]
            lines[b] = lines[a] + lines[b]
            lines[a].clear()

    for i in range(M):
        if lines[i]:
            print(*lines[i])
        else:
            print(-1)
    return


if __name__ == "__main__":
    N, M, Q = map(int, input().split())
    solution()