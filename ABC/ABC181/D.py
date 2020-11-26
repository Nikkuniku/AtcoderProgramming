s=input()

ans='No'
if len(s)==1:
    if int(s)%8==0:
        ans='Yes'
elif len(s)==2:
    if int(s)%8==0 or int(s[1]+s[0])%8==0:
        ans='Yes'
else:
    eight = []
    for i in range(13,125):
        eight.append(str(8*i))

    eight.append('000')

    from collections import Counter

    c=dict(Counter(s))

    for j in eight:
        d=c.copy()
        flg=0
        p=list(j)

        # 要素チェック
        for k in p:
            if k in d:
                d[k]-=1
            else:
                flg=1
                break
        
        # 要素がマイナス
        for g in d.values():
            if g<0:
                flg=1

        if flg==1:
            continue
        else:
            ans='Yes'
            break


print(ans)