N = int(input())
S = input()
T = input()
ans = 'Yes'
for i in range(N):
    s = S[i]
    t = T[i]
    if not (s == t or (s == '1' and t == 'l') or (t == '1' and s == 'l') or (s == '0' and t == 'o') or (s == 'o' and t == '0')):
        ans = 'No'
print(ans)
