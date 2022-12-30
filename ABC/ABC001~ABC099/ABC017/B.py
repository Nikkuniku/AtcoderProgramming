x=list(input())

x=list(reversed(x))


flg_ch=0
for i in range(len(x)):
    if flg_ch==0:
        if x[i]=='h' and i<len(x)-1:
            if x[i+1]=='c':
                flg_ch=1
            else:
                print('NO')
                exit(0)
        elif x[i]=='o':
            continue
        elif x[i]=='k':
            continue
        elif x[i]=='u':
            continue
        else:
            print('NO')
            exit(0)
    else:
        flg_ch=0
        continue

print('YES')