N=int(input())
H=list(map(int,input().split()))

max_h=H[0]

flg =0
for i in range(N):
    max_h =max(max_h,H[i])

    if max_h-1>H[i]:
        flg+=1

if flg!=0:
    print('No')
else:
    print('Yes')
