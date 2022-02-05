n,m=map(int,input().split())
pole=[]
existed=set()
place=[-1]*(n+1)
ans='Yes'
for _ in range(m):
    k=int(input())
    a=list(map(int,input().split()))
    t=0
    for b in a:
        if b not in existed:
            existed.add(b)
            place[b]=t
            t+=1
        else:
            k=place[b]
            if k>=t:
                t=k+1
                continue
            else:
                ans='No'

print(ans)