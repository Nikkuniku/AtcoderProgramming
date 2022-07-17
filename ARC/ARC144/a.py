n = int(input())
m = 2*n
cnt = n//4
ans = '4'*cnt
pre = n % 4
if pre != 0:
    ans = str(pre)+ans
print(m)
print(ans)
