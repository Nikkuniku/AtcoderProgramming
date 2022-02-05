n=int(input())
ans=0
for i in range(n):
    ans+=1/(n-i)

print(ans*n)