import sys
from collections import defaultdict
input = sys.stdin.readline


def solution(n:int, strs:list) -> None:
    for s in strs:
        cnts = defaultdict(int)
        for i in s:
            cnts[i] += 1
        cnt = sorted(cnts.keys(), key=lambda x: cnts[x], reverse=1)
        tmp = cnts[cnt[0]]
        aa = 0
        for c in cnt:
            if cnts[c] != tmp:
                break
            aa += 1
        if aa > 1:
            print("?")
        else:
            print(cnt[0])
        
    return



if __name__ == "__main__":
    n = int(input())
    strs = [input().strip() for _ in range(n)]
    solution(n, strs)