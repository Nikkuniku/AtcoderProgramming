d = int(input())
n = int(input())
at = [0]*(d+2)
for _ in range(n):
    l, r = map(int, input().split())
    at[l] += 1
    at[r+1] -= 1

for i in range(d+1):
    at[i+1] += at[i]

print(*at[1:d+1], sep="\n")
