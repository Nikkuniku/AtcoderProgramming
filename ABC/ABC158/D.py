S=input()
Q=int(input())

from collections import deque

S=deque(list(S))

flg=0

for i in range(Q):

    Query = list(input().split())
    
    if len(Query)!=1:
        F_i ,C_i = int(Query[1]),Query[2]
        
        if F_i==1 and flg==0:
            S.appendleft(C_i)
        
        elif F_i==2 and flg==0:
            S.append(C_i)   
        
        elif F_i==1 and flg==1:
            S.append(C_i)
        else:
            S.appendleft(C_i)
    else:
        if flg ==0:
            flg=1
        else:
            flg=0 

if flg ==1:
    S=reversed(S)

print(''.join(S))
