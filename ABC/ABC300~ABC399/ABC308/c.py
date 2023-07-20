from decimal import Decimal
N = int(input())
P = []
for i in range(N):
    a, b = map(int, input().split())
    P.append((i+1, Decimal(a)/Decimal(a+b)))
P.sort(key=lambda x: x[0])
P.sort(key=lambda x: x[1], reverse=True)
print(*[j for j, _ in P])
