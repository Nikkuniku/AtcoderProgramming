n=int(input())
a=list(map(int,input().split()))
degree=[0]
for i in range(n):
    p=(degree[-1]-a[i])%360
    degree.append(p)
degree.append(360)
degree.sort()

ans=0
for i in range(len(degree)-1):
    ans=max(ans,degree[i+1]-degree[i])
print(ans)