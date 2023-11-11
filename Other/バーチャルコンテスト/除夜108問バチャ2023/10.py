L1, R1, L2, R2 = map(int, input().split())
line = [0]*101
for i in range(L1, R1+1):
    line[i] += 1
for i in range(L2, R2+1):
    line[i] += 1
ans = line.count(2)
print(max(0, ans-1))
