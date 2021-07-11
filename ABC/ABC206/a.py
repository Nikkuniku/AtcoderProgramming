n=int(input())

import math
price =math.floor(1.08*n)

ans=':('
if price<206:
    ans='Yay!'
elif price==206:
    ans='so-so'
    

print(ans)