p = list(map(int,input().split()))

import collections
c= collections.Counter(p)

m=c.most_common()

m_1 = m[0]

if m_1[1]==2:
    ans=m[1][0]
elif m_1[1]==3:
    ans=m_1[0]
else:
    ans=0
    
print(ans)