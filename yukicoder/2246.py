N = int(input())
ans = []
for a in range(1, 10):
    for b in range(a+1, 10):
        X = 10*a + b
        ans.append(X)
ans.sort()
cnt = (N-1)//36
N %= 36
if N == 0:
    N = 36
res = ans[N-1]
res = str(res) + str(res)[-1]*cnt
print(res)
