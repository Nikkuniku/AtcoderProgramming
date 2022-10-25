n, a, b = map(int, input().split())
if a <= b:
    ans = n-a+1
else:
    k = (n-b+1)//a
    ans = b*k
    if (k+1)*a <= n:
        ans += n-(k+1)*a+1
print(max(ans, 0))
