from math import gcd

W, H = map(int, input().split())
g = gcd(W, H)
W //= g
H //= g
print("{0}:{1}".format(W, H))
