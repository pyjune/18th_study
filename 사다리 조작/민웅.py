# 15684_사다리조작_Ladder-control
# 지금 시간초과
import sys
input = sys.stdin.readline

def ladder_check(L, n):
    h = 0
    n_check = n
    while True:
        if h == H:
            break
        now = L[h][n_check]

        if now == 0:
            h += 1
        else:
            if L[h][n_check] == 'l':
                n_check += 1
            else:
                n_check -= 1
            h += 1

    if n_check == n:
        return True
    else:
        return False


def bt(l_lst, l_idx, ladder_now, picked):
    global ans
    global l_cnt

    if picked > 3:
        return

    if ans != -1:
        return

    for i in range(N):
        tmp = ladder_check(ladder_now, i)
        if not tmp:
            break
    else:
        ans = picked
        return

    while True:
        x, y = l_lst[l_idx]
        if ladder_now[x][y] == 0 and ladder_now[x][y+1] == 0:
            break

        if l_idx < l_cnt-1:
            l_idx += 1
        else:
            break
    if l_idx != l_cnt-1:
        bt(l_lst, l_idx+1, ladder_now, picked)

    x, y = l_lst[l_idx]
    ladder_now[x][y] = 'l'
    ladder_now[x][y+1] = 'r'
    bt(l_lst, l_idx, ladder_now, picked+1)
    ladder_now[x][y] = 0
    ladder_now[x][y+1] = 0



N, M, H = map(int, input().split())

ladder = [[0]*N for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 'l'
    ladder[a-1][b] = 'r'

l_sub = []
l_cnt = 0
for i in range(H):
    for j in range(N-1):
        if ladder[i][j] == 0 and ladder[i][j+1] == 0:
            l_sub.append([i, j])
            l_cnt += 1

ans = -1
if l_sub:
    bt(l_sub, 0, ladder, 0)
print(ans)