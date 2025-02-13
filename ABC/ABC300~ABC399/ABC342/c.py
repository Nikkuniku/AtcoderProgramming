from string import ascii_lowercase

N = int(input())
S = input()
Q = int(input())
alp = list(ascii_lowercase)
for _ in range(Q):
    c, d = input().split()
    for i, v in enumerate(alp):
        if v == c:
            alp[i] = d
ans = []
for i in range(N):
    ans.append(alp[ord(S[i]) - 97])
print(*ans, sep="")
