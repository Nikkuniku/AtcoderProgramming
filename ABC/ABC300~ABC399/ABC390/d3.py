N = int(input())
A = list(map(int, input().split()))

s = 0
for k in range(N):
    s ^= A[k]
# 一個ずつ
print(1, s)
# 2個
for i in range(N):
    for j in range(i + 1, N):
        a = A[i] + A[j]
        b = s ^ A[i] ^ A[j]
        print(2, i, j, a ^ b)
