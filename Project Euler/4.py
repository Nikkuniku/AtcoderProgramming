n=int(input())


ans=0

for i in range(n):
    for j in range(n):
        tmp=list(str(i*j))
        tmp_rv =list(reversed(tmp))

        flg=0
        for k in range(len(tmp)):
            if tmp[k]!=tmp_rv[k]:
                flg+=1

        if flg==0:
            ans=max(ans,int(''.join(tmp)))

print(ans)