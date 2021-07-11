n=int(input())
# 番兵を置く
a=list(map(int,input().split()))
a+=[0]

from collections import deque
q=deque()
ans=0
for i in range(n+1):
    if not q:
        q.append([a[i],i])
    else:
        v=q[-1]
        # スタック頂点の高さ
        v_h =v[0] 
        # スタック頂点のインデックス
        v_i =v[1]
        if v_h < a[i]:
            q.append([a[i],i])
        elif v_h > a[i]:
            target = i
            while q and q[-1][0] >= a[i]:
                w = q.pop()
                area = w[0] * ( i - w[1] )
                ans =max(ans,area)
                target = w[1]
            q.append([a[i],target])
    
print(ans)