res = []
for N in range(100, 110):
    s = set()
    for i in range(N + 1):
        if len(str(i)) == 2 and len(str(N - i)) == 2:
            s.add((i, N - i))
    print(len(s))
    res.append(len(s))
print("--")
print(sum(res))


def f(N):
    tmp = (81 * pow(10, N - 2) + 9 * pow(10, N - 1)) // 2
    tmp2 = (
        pow(10, 2 * N)
        - 2 * pow(10, 2 * N - 2)
        + ((pow(10, N - 1) - 1) * pow(10, N - 1) // 2)
    )
    return tmp + tmp2


print(f(2))
