n=int(input())
s=list(input())

from itertools import groupby

gr=groupby(s)
#flg=0:白の状態
flg=0
black=[]
white=[]
for k,v in gr:
    if flg==0 and k=='#':
        flg=1
        black.append(len(list(v)))
    elif flg==1:
        if k=='#':
            black.append(len(list(v)))
        else:
            white.append(len(list(v)))
if len(black)==0 or len(white)==0:
    print(0)
    exit(0)




cnt=sum(white)
ans=[cnt]
for i in range(len(white)):
    cnt+=(black[i]-white[i])
    ans.append(cnt)

print(min(ans))



