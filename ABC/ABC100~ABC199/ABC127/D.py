n,m = map(int,input().split())
cards = list(map(int,input().split()))

from collections import Counter

d = dict(Counter(cards))

for _ in range(m):
    b,c = map(int,input().split())

    if c in d:
        d[c]+=b
    else:
        d[c]=b

d= sorted(d.items(),key=lambda x: x[0],reverse=True)

ans = 0
cnt = 0
for j in d:
    cnt +=j[1]
    ans +=j[0] * j[1]



    if cnt>n:
        ans -=j[0]*(cnt-n)
        print(ans)
        exit(0)

print(ans)