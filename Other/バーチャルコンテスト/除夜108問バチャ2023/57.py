from itertools import groupby
S = input()
T = input()

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]


def runLengthEncode(S: str) -> "list[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


s = runLengthEncode(S)
t = runLengthEncode(T)
ans = 'Yes'
if len(s) != len(t):
    ans = 'No'
    print(ans)
    exit()
for i in range(len(s)):
    if s[i][0] != t[i][0]:
        ans = 'No'
        continue
    if s[i][1] == 1 and t[i][1] > 1:
        ans = 'No'
    if s[i][1] > t[i][1]:
        ans = 'No'
print(ans)
