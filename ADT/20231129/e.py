N, K = map(int, input().split())
A = set(list(map(int, input().split())))
for mex in range(K + 1):
    if mex not in A:
        break
print(mex)
