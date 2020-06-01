from decimal import *

a,b = map(Decimal,input().split())

import math
# a_1, a_2 = math.modf(a)
# b_1, b_2 =math.modf(b)

# total = math.floor(a_1*b_1) + math.floor(a_1*b_2) + math.floor(a_2*b_1) + math.floor(a_2 * b_2)

b*=100

ans = a*b

ans = ans //100

print(ans)