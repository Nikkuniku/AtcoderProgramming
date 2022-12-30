N = int(input())
A = list(map(int, input().split()))
ans = [0]*N
for i, v in enumerate(A, start=1):
    ans[v-1] += 1
print(*ans, sep="\n")
