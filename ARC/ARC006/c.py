n=int(input())
INF=10**8
boxes=[INF]*n

for _ in range(n):
    w=int(input())

    for i in range(n):
        if boxes[i]>=w:
            boxes[i]=w
            break

ans=n
for j in range(n):
    if boxes[j]==INF:
        ans-=1
print(ans)