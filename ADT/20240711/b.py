t = int(input())


def f(x):
    return x * x + 2 * x + 3


ans = f(f(f(t) + t) + f(f(t)))
print(ans)
