n=int(input())
ng1=int(input())
ng2=int(input())
ng3=int(input())

ngs=[ng1,ng2,ng3]
ans='YES'

if n in ngs:
    ans='NO'
    print(ans)
    exit(0)


if n<min(ngs):
    ans='YES'
    print(ans)
    exit(0)

if 3*min(ngs)+3 == sum(ngs):
    ans='NO'
    print(ans)
    exit(0)



n_300=[]
for i in range(100):
    n_300.append(300-3*i)

if n==300 and ((ng1 in n_300) or (ng2 in n_300) or (ng3 in n_300)):
    ans='NO'

tmp=n
for i in range(100):
    if (tmp-3 ) in ngs:
        if (tmp-2) in ngs:
            tmp-=1
        else:
            tmp-=2
    else:
        tmp-=3

if tmp<=0:
    ans='YES'
else:
    ans='NO'

print(ans)