N = int(input())
A = list(map(int, input().split()))
B = [(A[i], i) for i in range(N)]
B.sort()
B = B[::-1]
ans = B[1][1] + 1
print(ans)
