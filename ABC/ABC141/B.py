S=list(input())

odd = [S[i] for i in range(len(S)) if i%2==0]

even = [S[i] for i in range(len(S)) if i%2!=0]

flg=0
for s in odd:
    if s=='R' or s=='U' or s=='D':
        flg+=0
    else:
        flg+=1

for s in even:
    if s=='L' or s=='U' or s=='D':
        flg+=0
    else:
        flg+=1

if flg !=0:
    print('No')
else:
    print('Yes')