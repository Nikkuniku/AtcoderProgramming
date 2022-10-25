l1, r1, l2, r2 = map(int, input().split())
line = [-1]*(101)
for i in range(l1, r1):
    line[i] += 1
for i in range(l2, r2):
    line[i] += 1

ans = 0
for i in range(len(line)):
    if line[i] == 1:
        ans += 1
print(ans)
