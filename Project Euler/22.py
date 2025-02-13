from string import ascii_uppercase

f = open("./0022_names.txt", "r")
data = f.read().replace('"', "").split(",")
data.sort()


def calc(k, S):
    res = 0
    for s in S:
        idx = ascii_uppercase.index(s) + 1
        res += idx
    res *= k
    return res


ans = 0
for i, name in enumerate(data):
    ans += calc(i + 1, name)
print(ans)
