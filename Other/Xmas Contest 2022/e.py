N = int(input())
P = list(map(int, input().split()))
ans = 1
for p in P:
    ans *= p/100
print(ans)
