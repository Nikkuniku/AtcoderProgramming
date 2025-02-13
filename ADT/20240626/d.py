N = int(input())
A = list(map(int, input().split()))
for i in range(N - 1):
    s, t = map(int, input().split())
    k = A[i] // s
    A[i + 1] += t * k
print(A[-1])
