from decimal import Decimal, ROUND_HALF_UP
X, K = map(int, input().split())
for i in range(K):
    X = int(Decimal(X).quantize(Decimal('1E'+str(i+1)), rounding=ROUND_HALF_UP))
print(X)
