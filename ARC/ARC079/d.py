def check(arr):
    res = 0
    isEnd = False
    N = len(arr)
    while not isEnd:
        if all([a <= N - 1 for a in arr]):
            isEnd = True
            break
        idx = arr.index(max(arr))
        for i in range(N):
            arr[i] += -N if i == idx else 1
        res += 1
    return res, arr


A = list(map(int, input().split()))
print(check(A))
