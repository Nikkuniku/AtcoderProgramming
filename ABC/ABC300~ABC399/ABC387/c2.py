def f(X):
    res = 9
    if X < 10:
        return res
    k = X
    digits = []
    while k > 0:
        digits.append(k % 10)
        k //= 10
    L = len(digits)
    digits = digits[::-1]
    isSnake = True
    # 1
    for i in range(1, L):
        if digits[0] <= digits[i]:
            isSnake = False
            break
    res += 1 if isSnake else 0
    # 2
    for k in range(1, digits[0]):
        res += pow(k, L - 1)
    # 3
    for p in range(2, L):
        for k in range(1, 10):
            res += pow(k, p - 1)
    # 4
    for i in range(1, L):
        di = digits[i]
        minval = min(digits[0], di)
        res += minval * pow(digits[0], L - (i + 1))
        if digits[0] <= di:
            break
    return res


def isSnake(k):
    p = str(k)
    for i in range(1, len(p)):
        if int(p[0]) <= int(p[i]):
            return False
    return True


L, R = map(int, input().split())
ans = f(R) - f(L - 1)
print(ans)
