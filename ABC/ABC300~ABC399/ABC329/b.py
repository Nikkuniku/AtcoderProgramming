N = int(input())
A = list(map(int, input().split()))
maxA = max(A)
A = set(A)
A.discard(maxA)
print(max(A))
