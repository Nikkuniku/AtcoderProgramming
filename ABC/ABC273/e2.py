from collections import defaultdict
Q = int(input())
ad = []
sa = []
lo = []
dl = []
time = defaultdict(int)
Q = int(input())
ans = []
for i in range(Q):
    query = input().split()
    sql = query[0]
    if sql == 'ADD':
        x = query[1]
        ad.append(i)
    elif sql == 'DELETE':
        dl.append(i)
    elif sql == 'SAVE':
        y = query[1]
        sa.append(i)
        time[y] = i
    elif sql == 'LOAD':
        lo.append(i)


print(*ans)
