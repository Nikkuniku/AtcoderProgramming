
S = input()
N = len(S)
cnt = 0

for i in range(N-3):
    for j in range(i+4, N+1):
        if int(S[i:j]) % 2019 == 0:
            z = int(S[i:j])
            cnt += 1
            continue


print(cnt)

t = 2019
re = []
for i in range(1, 50):
    if '0' in str(t*i):
        continue
    re.append((t*i, i))
# print(re)
