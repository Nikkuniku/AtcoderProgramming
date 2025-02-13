A, B, O, W = map(int, input().split())
ans = O
if max(A, B) > 0:
    ans += max(A, B)
    ans += W
else:
    ans += W
print(ans)
