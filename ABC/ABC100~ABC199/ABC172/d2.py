n=int(input())
divs=[0]*(n+1)

for i in range(1,n+1):
    j=i
    while i<=n:
        divs[i]+=i
        i+=j

ans=sum(divs)

print(ans)