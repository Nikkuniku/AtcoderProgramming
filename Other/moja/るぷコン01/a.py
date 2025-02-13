from string import ascii_lowercase

N = int(input())
S = input()
c = input()
j = ascii_lowercase.index(S[0])
i = ascii_lowercase.index(c)
diff = (j - i) % 26
ans = []
for s in S:
    i = ascii_lowercase.index(s)
    now = i
    for _ in range(diff):
        now -= 1
        now %= 26
    ans.append(ascii_lowercase[now])
print(*ans, sep="")
