ans = 0
for i in range(12):
    S = input()
    ans += len(S) == i + 1
print(ans)
