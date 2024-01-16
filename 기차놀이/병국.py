from collections import deque
n,m,q = map(int,input().split())
# 1 2 3
# 4 5 6

# 첫번째놀이 > 1 2 3 >>> 2 3 1
# 두번째놀이 > 1 2 3 >>> 3 1 2 
#  2 3 1 > 3 1 2
#  456 > 645
# 세번째놀이 
train = [deque() for _ in range(m)]
idx = 1
for i in range(len(train)):
    for j in range(n//m):
        train[i].append(idx)
        idx+=1
# print(train)



for _ in range(q):
    arr = list(map(int,input().split()))
    # arr = [3,0,1]
    if arr[0] == 1:
        if train[arr[1]]:
            train[arr[1]].append(train[arr[1]].popleft())
    elif arr[0] == 2:
        if train[arr[1]]:
            train[arr[1]].appendleft(train[arr[1]].pop())
    elif arr[0] == 3:
        train[arr[2]] = train[arr[1]]+train[arr[2]]
        train[arr[1]] = deque()
# print(train)
        # aa = train.pop()
        # print(aa,'sad')
        # print(train,'asdqqq')\
# print(train)
for i in range(len(train)):
    if len(train[i]) == 0:
        print(-1)
    else:
        for j in train[i]:
            print(j, end= ' ')
        print()