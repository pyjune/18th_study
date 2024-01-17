def f(i, N, s):
    if i==N:
        ans.append(s)
    else:
        candidate = '01'
        if i>0 and s[i-1]=='1':
            candidate = '0'
        for j in candidate:
            f(i+1, N, s + j)


N = int(input())
ans = []
f(0, N, '')
print(ans)
