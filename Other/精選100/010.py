n=int(input())
a=list(map(int,input().split()))
q=int(input())
M=map(int,input().split())

candidate=set()
for i in range(1<<n):
    tmp=0
    for j in range(n):
        if (i>>j)&1:
            tmp+=a[j]
    
    candidate.add(tmp)

for m in M:
    ans='no'
    if m in candidate:
        ans='yes'
    print(ans)