S=input()
length = len(S)//2

cnt = 0
S_rev = S[::-1]

for i in range(length):
    if S[i] != S_rev[i]:
        cnt+=1

print(cnt)
