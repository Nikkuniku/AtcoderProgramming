X=int(input())

import math

year = 0
money=100
while money<X:
    money=math.floor(money * 1.01)
    year+=1

print(year)