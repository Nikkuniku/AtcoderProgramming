n=int(input())

ans =[]
from collections import deque 
for i in range(2**n):
    tmp_array=deque([])
    tmp_sum=[0]
    for j in range(n-1,-1,-1):
        if ((i>>j)&1):
            tmp_array.append(1)
            p=tmp_sum[-1]+1
        else:
            tmp_array.append(-1)
            p=tmp_sum[-1]-1
        tmp_sum.append(p)

    if tmp_sum[-1]!=0:
        continue    

    for l in range(len(tmp_sum)):
        if tmp_sum[l]>0:
            break
    else:
        ans.append(tmp_array)

ans=sorted(ans)
for m in range(len(ans)):
    ot=''
    for o in ans[m]:
        if o==-1:
            ot+='('
        else:
            ot+=')'
    print(ot)
