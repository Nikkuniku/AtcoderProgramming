from itertools import groupby

N=input()
array =[i for i in N]

gr =groupby(array)

flg = 0
for key,group in gr:
    if len(list(group))>=3:
        flg+=1

if flg ==0:
    print('No')
else:
    print('Yes')
    