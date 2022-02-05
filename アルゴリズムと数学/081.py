n=int(input())
ans=0

while n>0:
    if n>=10000:
        n-=10000
    elif n>=5000:
        n-=5000
    elif n>=1000:
        n-=1000
    ans+=1
print(ans)