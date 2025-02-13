N = int(input())
ans = 1
for i in range(1, N + 1):
    if i * i * i > N:
        break
    s = list(str(i * i * i))
    if s == s[::-1]:
        ans = i * i * i
print(ans)
