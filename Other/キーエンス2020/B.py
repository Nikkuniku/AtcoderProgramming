n=int(input())
r=[]
for _ in range(n):
    s,t=map(int,input().split())

    r.append([s-t,s+t])

r=sorted(r,key=lambda x: x[1])


ans=[r[0]]
for i in range(1,n):
    if r[i][0]>=ans[-1][1]:
        ans.append(r[i])

        


print(len(ans))