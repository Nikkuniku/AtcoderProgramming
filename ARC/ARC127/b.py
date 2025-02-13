def base_n(num_10, n):
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return str_n[::-1]


N, L = map(int, input().split())

base = []
for i in range(N):
    tmp = 2 * pow(3, L - 1) + i
    tmp = base_n(tmp, 3)
    base.append(tmp)
d = dict()
d["0"] = "1"
d["1"] = "2"
d["2"] = "0"
ans = []
for s in base:
    ans.append("".join([d[si] for si in s]))
for i in range(N):
    ans.append("".join([d[si] for si in ans[i]]))
ans += base
print(*ans, sep="\n")
