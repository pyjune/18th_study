import sys
input = sys.stdin.readline

def bt(n, word, before):
    global ans
    if len(word) == n:
        ans.append(word)
        return

    if before != '1':
        bt(n, word+'0', '0')
        bt(n, word+'1', '1')
    else:
        bt(n, word + '0', '0')

N = int(input())
ans = []

bt(N, '', '')
print(ans)