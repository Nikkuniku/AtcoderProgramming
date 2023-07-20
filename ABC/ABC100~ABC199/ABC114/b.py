S = input()
ans = 1 << 60
for i in range(len(S)-2):
    tmp = int(S[i:i+3])
    ans = min(ans, abs(tmp-753))
print(ans)
