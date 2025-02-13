L = int(input())
A = [0]
for i in range(L):
    b = int(input())
    # ai^ai+1=bより、ai+1=ai^bである。
    if i == L - 1:
        if A[0] ^ A[L - 1] != b:
            exit(print(-1))
    else:
        A.append(A[-1] ^ b)
print(*A, sep="\n")
