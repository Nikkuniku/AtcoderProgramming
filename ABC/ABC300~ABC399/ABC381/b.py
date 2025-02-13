from string import ascii_lowercase

S = input()
N = len(S)
alp = [0] * 26
ans = "Yes"
if N % 2 != 0:
    exit(print("No"))
for i in range(N // 2):
    si, ti = S[2 * i], S[2 * i + 1]
    if si != ti:
        ans = "No"
    alp[ascii_lowercase.index(si)] += 1
    alp[ascii_lowercase.index(ti)] += 1
for v in alp:
    if v != 0 and v != 2:
        ans = "No"
print(ans)
