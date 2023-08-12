a, b, c = map(int, input().split())
ans = [2]*(a+b+c)
N = int(input())
result = [list(map(int, input().split())) for _ in range(N)]
result.sort(key=lambda x: x[3], reverse=True)
for x, y, z, r in result:
    if r == 1:
        ans[x-1] = 1
        ans[y-1] = 1
        ans[z-1] = 1
    else:
        tmp = sum([ans[p-1] == 1 for p in [x, y, z]])
        if tmp == 2:
            for k in [x, y, z]:
                if ans[k-1] != 1:
                    ans[k-1] = 0
print(*ans, sep="\n")
