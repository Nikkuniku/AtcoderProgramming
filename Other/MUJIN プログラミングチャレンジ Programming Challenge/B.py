la,lb,lc=map(int,input().split())
from math import acos
r = la+lb+lc
S_c = acos(-1)*(r**2)

s_a=0
if la+lb>lc and lb+lc>la and lc+la>lb:
    s_a=0
elif la>lb+lc:
    s_a = acos(-1)*((la-lb-lc)**2)
elif lb > la+lc :
    s_a = acos(-1)*((lb-la-lc)**2)
elif lc > la+lb:
    s_a = acos(-1)*((lc-la-lb)**2)

print(S_c-s_a)