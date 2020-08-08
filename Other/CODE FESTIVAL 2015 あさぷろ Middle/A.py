n,k,m,r = map(int,input().split())

s=[]
for _ in range(n-1):
    tmp=int(input())
    s.append(tmp)

s=sorted(s,reverse=True)
ave1=sum(s[:k])/k

if ave1>=r:
    print(0)
else:
    s_n = k*r - sum(s[:k-1])

    if s_n<=m:
        print(s_n)
    else:
        print(-1)