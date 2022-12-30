from functools import lru_cache
n = int(input())


@lru_cache
def f(X):
    if X == 0:
        return 1
    X1 = X // 2
    X2 = X // 3
    return f(X1) + f(X2)


ans = f(n)
print(ans)
