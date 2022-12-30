N = int(input())
A = list(map(lambda x: int(x)+1, input().split()))
# BIT
data = [0]*(N+1)


def add(k, x):
    while k <= N:
        data[k] += x
        k += k & -k


def get(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s


res = 0
for i, a in enumerate(A):
    # 自分より小さい要素がいくつ存在するかを計算
    res += (N-1-i) - get(a)
    add(a, 1)

ans = [res]
for i in range(N-1):
    res -= A[i]-1
    res += N-1-(A[i]-1)
    ans.append(res)
print(*ans, sep="\n")
