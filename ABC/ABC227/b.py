from typing import AnyStr


n=int(input())
s=list(map(int,input().split()))

ans=0
for i in range(n):
    flg=1
    s_i=s[i]
    for a in range(1,200):
        for b in range(1,200):
            if s_i == 4*a*b +3*a+3*b:
                flg=0
            
            if flg==0:
                continue
        if flg==0:
             continue
    
    ans+=flg

print(ans)
