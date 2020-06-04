n=int(input())

d=[0]*(10**5)
cnt = 0

for _ in range(n):
    a=int(input())
    a-=1
    if d[a]==1:
        cnt+=1
    else:
        d[a]=1

print(cnt)