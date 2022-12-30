N,M = map(int,input().split())

Peaks = list(map(int,input().split()))

ans =[1]*N

for i in range(M):
    a,b = map(int,input().split())
    a=a-1
    b=b-1

    if Peaks[a]>Peaks[b]:
        ans[b]=0
    elif Peaks[a]<Peaks[b]:
        ans[a]=0
    else:
        ans[a]=0
        ans[b]=0

print(sum(ans))
