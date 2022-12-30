n=int(input())
a = list(map(int,input().split()))

from collections import Counter

c = Counter(a)

cnt=0
for i in c.items():
    if i[0]==i[1]:
        continue
    elif i[0]>i[1]:
        cnt+=i[1]
    elif i[0]<i[1]:
        cnt+=(i[1]-i[0])

print(cnt)