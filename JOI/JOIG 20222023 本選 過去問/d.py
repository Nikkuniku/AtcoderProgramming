H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
row = [sum([S[i][j] == '#' for j in range(W)]) for i in range(H)]
column = [sum([S[i][j] == '#' for i in range(H)]) for j in range(W)]
total = sum(row)
ans = []
for i in range(H):
    rin = -1
    for j in range(W):
        p = 1 if S[i][j] == '#' else 0
        diff_omote = H+W + 2*(2*p-1-row[i]-column[j])
        tmp_total = total+diff_omote
        if H*W-tmp_total > rin:
            rin = H*W-tmp_total
    ans.append((H*W-rin, rin))
ans.sort()
print(*ans[::-1][0])
