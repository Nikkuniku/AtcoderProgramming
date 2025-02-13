N, R = map(int, input().split())
for _ in range(N):
    d, a = map(int, input().split())
    if d == 1:
        if 1600 <= R <= 2799:
            R += a
    elif d == 2:
        if 1200 <= R <= 2399:
            R += a
print(R)
