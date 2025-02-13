def naiseki(X, Y):
    return X[0] * Y[0] + X[1] * Y[1]


A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = "No"
AB = [B[0] - A[0], B[1] - A[1]]
AC = [C[0] - A[0], C[1] - A[1]]
BA = [A[0] - B[0], A[1] - B[1]]
BC = [C[0] - B[0], C[1] - B[1]]
CA = [A[0] - C[0], A[1] - C[1]]
CB = [B[0] - C[0], B[1] - C[1]]
if naiseki(AB, AC) == 0 or naiseki(BA, BC) == 0 or naiseki(CA, CB) == 0:
    ans = "Yes"
print(ans)
