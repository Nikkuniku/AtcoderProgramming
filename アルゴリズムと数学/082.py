n=int(input())
eiga=[]
for _ in range(n):
    eiga.append(list(map(int,input().split())))
eiga.sort(key=lambda x:x[0])
eiga.sort(key=lambda x:x[1])

cur=0
ans=0
for i in range(n):
    p=eiga[i]
    if cur<=p[0]:
        cur=p[1]
        ans+=1

print(ans)