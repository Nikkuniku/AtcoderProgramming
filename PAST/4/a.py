A = list(map(int, input().split()))
B = [(A[i], "ABC"[i]) for i in range(3)]
B.sort()
print(B[1][1])
