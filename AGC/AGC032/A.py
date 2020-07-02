n=int(input())
b=list(map(int,input().split()))

for i in range(n):
    if i+1<b[i]:
        print(-1)
        exit(0)


from collections import deque

d=deque([])

while len(d)<n:
    tmp=b
    for j in range(len(tmp)-1,-1,-1):
        if j+1==tmp[j]:
            d.append(tmp[j])
            break

    b.pop(j)


for _ in range(n):
    v=d.pop()
    print(v)
