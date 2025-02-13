N, L, R = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for a in A:
    if a <= L:
        ans.append(L)
    elif R <= a:
        ans.append(R)
    else:
        ans.append(a)
print(*ans)
