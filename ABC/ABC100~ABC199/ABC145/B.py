N=int(input())
S=input()

if N==1 or N%2!=0:
    print('No')
    exit(0)

S_pre = S[:int(N/2)]
S_aft = S[int(N/2):]

flg=0
for i in range(len(S_pre)):
    if S_pre[i] != S_aft[i]:
        flg+=1

if flg==0:
    print('Yes')
else:
    print('No')