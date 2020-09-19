n=int(input())
d1=[]
d2=[]

for _ in range(n):
    D1,D2 = map(int,input().split())

    d1.append(D1)
    d2.append(D2)

ans='No'

cnt=0
for i in range(n):
    p=d1[i]
    q=d2[i]

    if p==q:
        cnt+=1
    else:
        cnt=0

    if cnt>=3:
        ans='Yes'
        break


print(ans)


