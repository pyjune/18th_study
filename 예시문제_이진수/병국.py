def make(a, nownum, last):
    if len(nownum) == a:
        return [nownum]
    answer = []
    answer += make(a, nownum + '0', 0)
    if last != 1:
        answer += make(a, nownum + '1', 1)
    return answer



n = int(input())

cnt = 0
cnt = make(n,'',0)
print(cnt)
