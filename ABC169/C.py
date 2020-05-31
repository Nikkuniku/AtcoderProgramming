a,b = map(float,input().split())

import math
# a_1, a_2 = math.modf(a)
# b_1, b_2 =math.modf(b)

# total = math.floor(a_1*b_1) + math.floor(a_1*b_2) + math.floor(a_2*b_1) + math.floor(a_2 * b_2)

b*=1000

ans = a*b

ans = ans /1000

print(int(ans))