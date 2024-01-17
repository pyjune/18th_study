import sys
input = sys.stdin.readline


def bt(N:int, binary:str):
    global ans
    if len(binary) == N:
        ans.add(binary)
        return 
    bt(N, binary+"0")
    if binary and binary[-1] != '1':
        bt(N, binary+"1")
    return


if __name__ == "__main__":
    N = int(input())
    ans = set()
    bt(N,"")
    print(sorted(list(ans)))