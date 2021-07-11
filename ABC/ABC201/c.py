s=input()

ans=0
for i in range(10000):
    i_str = list(str(i).zfill(4))
    flg=0
    for j in range(10):
        if s[j]=='o':
            if str(j) not in i_str:
                flg+=1
                break
        elif s[j]=='x':
            if str(j) in i_str:
                flg+=1
                break

    if flg>0:
        continue
    ans+=1

print(ans)