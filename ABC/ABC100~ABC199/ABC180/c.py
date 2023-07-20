N = int(input())
ans = set()
for i in range(1, N+1):
    if i*i > N:
        break
    if N % i == 0:
        ans.add(i)
        ans.add(N//i)
ans = sorted(list(ans))
print(*ans, sep="\n")
