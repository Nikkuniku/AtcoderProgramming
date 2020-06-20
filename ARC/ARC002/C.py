n=int(input())
s=input()

if n<=2:
    print(1)
    exit(0)
strings=['AA','AB','AX','AY','BA','BB','BX','BY','XA','XB','XX','XY','YA','YB','YX','YY']
from itertools import combinations

c=list(combinations(strings,2))

cnt=10**9
for i in c:
    a=i[0]
    b=i[1]
    flg=0
    tmp=0
    for j in range(n-1):
        if flg==0:
            if j!=n-2:
                if ((s[j]==a[0] and s[j+1]==a[1]) or (s[j]==b[0] and s[j+1]==b[1])):
                    tmp+=1
                    flg=1
                else:
                    tmp+=1
            else:
                if ((s[j]==a[0] and s[j+1]==a[1]) or (s[j]==b[0] and s[j+1]==b[1])):
                    tmp+=1
                else:
                    tmp+=2
        else:
            if j==n-2:
                tmp+=1
            else:
                flg=0

    cnt=min(tmp,cnt)

print(cnt)

    