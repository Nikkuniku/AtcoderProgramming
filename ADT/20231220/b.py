N, A, B = map(int, input().split())
C = list(map(int, input().split()))
idx = C.index(A + B)
print(idx + 1)
