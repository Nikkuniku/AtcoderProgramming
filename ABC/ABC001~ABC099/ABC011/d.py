from math import factorial

N, D = map(int, input().split())
X, Y = map(int, input().split())
if X % D != 0 or Y % D != 0:
    exit(print(0))
a = X // D
b = Y // D
c = factorial(a + b) / (factorial(a) * factorial(b))
ans = c / pow(4, a + b)
print(ans)
