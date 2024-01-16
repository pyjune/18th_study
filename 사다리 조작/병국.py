def check():
    for i in range(N):
        now = i
        for j in range(H):
            if ladder[j][now] == 1:
                now += 1
            elif now >= 1 and ladder[j][now-1] == 1:
                now -= 1
        # 하나라도 시작이랑 도착 다르면 바로 리턴
        if now != i:
            return False
    return True

def back(cnt, x, y):
    global answer
    if check(): # True면 된다는거
        answer = min(cnt,answer)
        return
    elif cnt == 3 or answer <= cnt:
        return

    # 가로선 탐색해보자,
    for i in range(x, H):
        # 아직 x행 보고 있으면
        if i == x:
            # 가로선 고정
            tmp = y
        else:
            tmp = 0
        # 세로선
        for j in range(tmp, N-1):
            # 내위치, 오른쪽위치에 사다리없으면
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                # 근데 왼쪽에있다면..? 일직선되니까 패스
                if j > 0 and ladder[i][j-1] == 1:
                    continue
                ladder[i][j] = 1
                # 행은 같은데 열은 두칸뒤로 가야된다, 일직선 되면 안되니까.
                back(cnt+1,i,j+2)
                ladder[i][j] = 0


N, M, H = map(int,input().split())
ladder = [[0]*(N) for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    ladder[a-1][b-1] = 1
# print(ladder)

answer = 4
back(0, 0, 0)
if answer < 4:
    print(answer)
else:
    print(-1)