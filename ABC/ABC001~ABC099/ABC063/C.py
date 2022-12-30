n=int(input())

score=[]
for _ in range(n):
    s=int(input())
    score.append(s)

#すべて10の倍数ならば0である
non10=[]
flg10=0
for i in range(n):
    if score[i]%10!=0:
        non10.append(score[i])
        flg10=1
    
if flg10==0:
    ans=0
else:
    if sum(score)%10==0:
        ans=sum(score)-min(non10)
    else:
        ans=sum(score)
print(ans)
    
