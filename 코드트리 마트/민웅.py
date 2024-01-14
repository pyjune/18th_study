import sys
import heapq
# from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
customers = []

for i in range(1, N+1):
    t, s = map(int, input().split())
    heapq.heappush(customers, [t, s, i])


first = heapq.heappop(customers)
time = first[0]
q = []
heapq.heappush(q, [-1*first[1], first])
ans = []

while customers or q:
    while True:
        if customers:
            tmp = heapq.heappop(customers)
            # print("tmp는", tmp)
            if tmp[0] <= time:
                # print("들어간 tmp", tmp)
                heapq.heappush(q, [-1*tmp[1], tmp])
            else:
                heapq.heappush(customers, tmp)
                # print(q)
                break
        else:
            break
    # q.sort(key=lambda x: (-1*x[1]))
    cus = heapq.heappop(q)
    ans.append(cus[1][2])
    time += K
    # print(time)
print(*ans)