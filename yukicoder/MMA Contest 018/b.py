from collections import Counter
from string import ascii_uppercase

N = int(input())
S = input()
alp = [0] * 26
C = Counter(S)
for s in ascii_uppercase:
    alp[ord(s) - 65] = C[s]
print(*alp, sep="")
