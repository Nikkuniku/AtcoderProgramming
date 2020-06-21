n=int(input())
a=list(map(int,input().split()))
q=int(input())

s=sum(a)
d=[0]*(10**5+1)
for i in a:
    d[i-1]+=1

for _ in range(q):
    b,c=map(int,input().split())
    tmp=0
    k=d[b-1]
    d[c-1]+=k
    d[b-1]=0

    tmp = k*c-k*b
    s+=tmp
    print(s)
