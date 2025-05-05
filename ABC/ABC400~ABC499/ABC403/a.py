N = int(input())
A = list(map(int, input().split()))
ans = sum([A[i] * (1 - i % 2) for i in range(N)])
print(ans)
