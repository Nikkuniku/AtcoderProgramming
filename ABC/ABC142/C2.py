n=int(input())
a=list(map(int,input().split()))

b=[]
for i in range(n):
    tmp=[i+1,a[i]]
    b.append(tmp)

b=sorted(b,key=lambda x:x[1])


ans=[]
for j in b:
    ans.append(j[0])

print(*ans)