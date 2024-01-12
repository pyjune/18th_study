import sys, heapq
input = sys.stdin.readline


def solution(N:int, K:int, wait:list) -> list:
    sequence = [0] * N
    que = []
    now, last = 0, 0
    heapq.heappush(que, (-wait[0][2], wait[0][1], wait[0][0]))
    time = wait[0][1]
    while que:
        weight, t, idx = heapq.heappop(que)
        sequence[now] = idx
        now += 1
        time += K
        for w in range(last+1, N):
            if wait[w][1] <= time:
                heapq.heappush(que, (-wait[w][2], wait[w][1], wait[w][0]))
                last = w
            else:
                break
    return sequence


if __name__ == "__main__":
    N, K = map(int, input().split())
    wait = []
    for idx in range(N):
        t, s = map(int, input().split())
        wait.append((idx+1, t, s))
    wait.sort(key=lambda x:(x[1],-x[2]))
    ans = solution(N, K, wait)
    print(" ".join(list(map(str, ans))))