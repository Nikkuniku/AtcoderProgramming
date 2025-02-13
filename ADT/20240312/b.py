N = list(input())
ans = "Yes"
for i in range(1, len(N)):
    s = int(N[i])
    t = int(N[i - 1])
    if t <= s:
        ans = "No"
print(ans)
