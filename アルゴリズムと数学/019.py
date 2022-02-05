from collections import defaultdict
d=defaultdict(lambda:0)
n=int(input())
a=list(map(int,input().split()))


for i in range(n):
    d[a[i]]+=1

x=d[1]
y=d[2]
z=d[3]

def bi(p):
    return (p*(p-1))//2

ans=bi(x)+bi(y)+bi(z)
print(ans)