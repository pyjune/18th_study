n = int(input())
for _ in range(n):
    dict = {}
    arr = list(input())
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    maxx = 0
    answer = ''
    flag = True
    for i in (dict):
        # print(dict[i])
        if dict[i] > maxx:
            maxx = dict[i]
            answer = i
            flag = True
        elif dict[i] == maxx:
            flag = False
    if flag == True:
        print(answer)
    else:
        print("?")