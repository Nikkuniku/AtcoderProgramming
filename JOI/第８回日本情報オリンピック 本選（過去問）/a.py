N = int(input())
M = int(input())
S = input()
# IOIOIOIOI...のIから始まってIで終わるような文字列を抽出する
dp = [0]*M
for i in range(2, M):
    if S[i-2] == 'I' and S[i-1] == 'O' and S[i] == 'I':
        dp[i] = dp[i-2]+1
        dp[i-2] = 0
ans = 0
for c in dp:
    if c >= N:
        ans += c-N+1
print(ans)
