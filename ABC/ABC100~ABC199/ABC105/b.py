N = int(input())
ans = "No"
for x in range(26):
    for y in range(16):
        if 4 * x + 7 * y == N:
            ans = "Yes"
print(ans)
