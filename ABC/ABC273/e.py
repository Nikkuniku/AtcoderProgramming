from collections import defaultdict
a = []
d = defaultdict(int)
cn=defaultdict(int)
ans = []
Q = int(input())
cnt=0
for i in range(Q):
    query = input().split()
    sql = query[0]
    if sql == 'ADD':
        x = query[1]
        a.append(x)
        cnt+=1
    elif sql == 'DELETE':
        if cnt>0:
            a.pop()
            cnt-=1
            if a:
                ans.append(a[-1])
        else:
            ans.append(-1)
    elif sql == 'SAVE':
        y = query[1]
        d[y] = i
        ans.append(ans[-1])
    elif sql == 'LOAD':
        z = query[1]
        t=d[z]
        ans.append(ans[t])
    cn[i]=cnt

print(*ans)
