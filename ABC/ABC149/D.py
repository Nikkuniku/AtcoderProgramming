n,k=map(int,input().split())
r,s,p = map(int,input().split())
T=list(input())

a=[[] for i in range(k)]
for i in range(n):
    a[i%k].append(T[i])

d={'r':p,'s':r,'p':s}
score=0
for j in range(k):
    b=a[j]
    flg=0
    for l in range(len(b)):
        if l==0:
            score+=d[b[l]]
        else:
            if b[l-1]==b[l] and flg==0:
                flg=1
                continue
            elif b[l-1]==b[l] and flg==1:
                score+=d[b[l]]
            elif b[l-1]!=b[l]:
                score+=d[b[l]]
            flg=0
print(score)


