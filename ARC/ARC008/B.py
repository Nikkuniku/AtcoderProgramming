n,m=map(int,input().split())
name=input()
kit=input()

from collections import Counter

c_n=Counter(name)
c_kit=dict(Counter(kit))

#文字がkitにあるか確認
for key in c_n.keys():
    if key not in c_kit:
        print(-1)
        exit(0)

import math
ans=1
for k,v in c_n.items():
    #kitで足りる
    if c_kit[k]>=v:
        continue
    #kitで足りない
    else:
        if v>c_kit[k]:
            dif = v-c_kit[k]
            ans=max(ans,math.ceil(v/c_kit[k]))
print(ans)