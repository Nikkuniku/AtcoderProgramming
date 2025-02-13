A, B, C, D = map(int, input().split())
a = [0] * 101
for i in range(A, B):
    a[i] += 1
for i in range(C, D):
    a[i] += 1
ans = a.count(2)
print(ans)
