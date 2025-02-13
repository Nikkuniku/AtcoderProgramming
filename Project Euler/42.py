from string import ascii_uppercase

f = open("./0042_words.txt", "r")
data = f.read().replace('"', "").split(",")


def calc(S):
    res = 0
    for s in S:
        idx = ascii_uppercase.index(s) + 1
        res += idx
    return res


Triangle = set()
for n in range(1, 21):
    Triangle.add(n * (n + 1) // 2)

ans = 0
for word in data:
    if calc(word) in Triangle:
        ans += 1
print(ans)
