import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    msg = input().strip()
    msg_dict = {}

    max_cnt = 0
    ans = ''
    ans_check = False
    for i in range(len(msg)):
        tmp = msg[i]
        if tmp in msg_dict.keys():
            msg_dict[tmp] += 1
        else:
            msg_dict[tmp] = 1

    for key, item in msg_dict.items():
        if item > max_cnt:
            ans = key
            max_cnt = item
            ans_check = False
        elif item == max_cnt:
            ans_check = True
    
    if ans_check:
        print('?')
    else:
        print(ans)