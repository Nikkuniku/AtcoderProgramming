n, l, w = map(int, input().split())
ans = 0
a = [0]+list(map(int, input().split()))+[l]
n += 2
for i in range(n-1):
    if i == 0:
        ans += max(-(-(a[i+1]-a[i])//w), 0)
    else:
        ans += max(-(-(a[i+1]-a[i])//w)-1, 0)
print(ans)
