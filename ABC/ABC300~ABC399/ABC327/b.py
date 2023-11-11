B = int(input())
ans = -1
for a in range(1, 20):
    if pow(a, a) == B:
        ans = a
print(ans)
