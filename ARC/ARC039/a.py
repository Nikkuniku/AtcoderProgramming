A, B = input().split()
ans = -(1 << 60)
# Aを変更する
for i in range(3):
    tmp = list(A)[:]
    if i == 0:
        for j in range(1, 10):
            tmp[i] = str(j)
            ans = max(int("".join(tmp)) - int(B), ans)
    else:
        for j in range(10):
            tmp[i] = str(j)
            ans = max(int("".join(tmp)) - int(B), ans)
# Bを変更する
for i in range(3):
    tmp = list(B)[:]
    if i == 0:
        for j in range(1, 10):
            tmp[i] = str(j)
            ans = max(int(A) - int("".join(tmp)), ans)
    else:
        for j in range(10):
            tmp[i] = str(j)
            ans = max(int(A) - int("".join(tmp)), ans)
print(ans)
