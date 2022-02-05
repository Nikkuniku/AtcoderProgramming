n=int(input())

ans=[]
tmp=n
for i in range(2,int(n**0.5)+1):
    if tmp%i==0:
        while tmp%i==0:
            tmp//=i
            ans.append(i)
if tmp!=1:
    ans.append(tmp)

print(*ans)