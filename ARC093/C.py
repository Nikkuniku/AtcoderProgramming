n=int(input())
a= list(map(int,input().split()))

b=[0] + a + [0]
now=0
dist=0


for i in range(n+1):
    dist += abs(b[i+1] - b[i])

for i in range(1,n+1):
    ans=0
    
    d1 = abs(b[i-1] - b[i+1])
    d2 = abs(b[i]-b[i-1])
    d3 = abs(b[i+1]-b[i])

    ans = dist+d1-(d2+d3) 

    print(ans)




