import bisect
n = int(input())
a = list(map(int, input().split()))
p = [[]for _ in range(n+1)]


for i in range(n):
    p[a[i]].append(i+1)

q = int(input())
answer = []
for _ in range(q):
    l, r, x = map(int, input().split())
    i = bisect.bisect_right(p[x], r)
    j = bisect.bisect_left(p[x], l)
    answer.append(i-j)
print(*answer, sep="\n")
