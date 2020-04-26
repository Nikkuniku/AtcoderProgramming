S=input()
S_reverse =S[::-1]

N=len(S)
#1.回文の判定
# for i in range()
flg1 = 0
for i in range(N//2):
    if S[i] != S_reverse[i]:
        flg1+=1

# 2.前半部分は回文
S_pre =S[:N//2]
S_pre_reverse=S_pre[::-1]


flg2=0
if S_pre != S_pre_reverse:
    flg2+=1

# 3.後半部分は回文
S_last = S[int((N+3)/2)-1:]
S_last_reverse = S_last[::-1]

flg3 = 0
if S_last != S_last_reverse:
    flg3 +=1

if flg1 ==0 and flg2 ==0 and flg3==0:
    print('Yes')
else:
    print('No')
