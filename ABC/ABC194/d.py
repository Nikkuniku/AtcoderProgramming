n=int(input())
ans=0
for i in range(1,n):
    ans+=1/(n-i)
ans*=n
print(ans)