def mat_rotate(A):
    res = [A[i][::-1] for i in range(len(A))][::-1]
    return res


C = [list(input()) for _ in range(2)]
ans = "YES" if C == mat_rotate(C) else "NO"
print(ans)
