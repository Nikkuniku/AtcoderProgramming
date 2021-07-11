n=int(input())
p=[]
l=0
r=0
for i in range(n):
    a,b=map(int,input().split())

    r+=a
    p.append([a,b,2*a+b])

# p=sorted(p,key=lambda x: x[1],reverse=True)
# p=sorted(p,key=lambda x: x[0],reverse=True)
p=sorted(p,key=lambda x: x[2],reverse=True)

ans=0
for i in range(n):
    l+=p[i][0]+p[i][1]
    r-=p[i][0]
    ans+=1

    if l>r:
        break

print(ans)