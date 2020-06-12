n=int(input())
d= list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))

if n<m:
    print('NO')
    exit(0)

pro={}
for i in d:
    if i in pro:
        pro[i]+=1
    else:
        pro[i]=1

for j in t:
    if j in pro:
        if pro[j]>0:
            pro[j]-=1
        else:
            print('NO')
            exit(0)
    else:
        print('NO')
        exit(0)

print('YES')