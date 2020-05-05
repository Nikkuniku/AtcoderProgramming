N=int(input())
Students=list(map(int,input().split()))


d={}

for i in range(N):
    d[i+1]=Students[i]

d_2 = sorted(d.items(),key=lambda x: x[1])

ans=[]
for k in d_2:
    ans.append(k[0])

print(*ans)