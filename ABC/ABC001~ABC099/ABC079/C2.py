s=list(input())

from itertools import product as pr

p = list(pr(['+','-'],repeat=3))

for ope in p:
    f = s[0] + ope[0] + s[1] + ope[1] + s[2] + ope[2] + s[3]

    if eval(f)==7:
        print(f+'=7')
        exit(0)

