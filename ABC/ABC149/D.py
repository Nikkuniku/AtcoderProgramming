N,K=map(int,input().split())

r,s,p = map(int,input().split())

T=list(input())

T=''.join(list(reversed(T)))

d={}
for j in range(N):
    if T[j]=='r':
        d[j]=p
    elif T[j]=='s':
        d[j]=r
    else:
        d[j]=s

for i in range(N):
    if i-K in d:
        if d[i]==d[i-K]:
            d[i]=0

score=0

for _,val in d.items():
    score+=val

print(score)
