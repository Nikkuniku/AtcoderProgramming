def solve(s):
    if len(s) == s.count('a'):
        return -1
    if s[0] != 'a' or 'atcoder' < s:
        return 0
    for j in range(1, len(s)):
        if 't' < s[j]:
            return j-1
        elif 'a' < s[j] <= 't':
            return j


T = int(input())
ans = []
for _ in range(T):
    S = input()
    ans.append(solve(S))
print(*ans, sep="\n")
