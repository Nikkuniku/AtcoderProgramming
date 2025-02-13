l1, r1, l2, r2 = map(int, input().split())
A = [0] * 101
for i in range(l1, r1):
    A[i] += 1
for i in range(l2, r2):
    A[i] += 1
print(A.count(2))
