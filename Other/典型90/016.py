n=int(input())
a,b,c = map(int,input().split())
coins=sorted([a,b,c])

c1 = coins[2]
c2 = coins[1]
c3 = coins[0]
ans=10000

for i in range(10000):
    if c1*i>n:
        continue
    for j in range(10000-i):
        if c1*i +c2*j>n:
            continue

        if (n-c1*i-c2*j)%c3==0:
            k = (n-c1*i-c2*j)//c3
            ans=min(ans,i+j+k)

print(ans)