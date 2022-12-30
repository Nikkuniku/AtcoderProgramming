n = int(input())
h = list(map(int, input().split()))
maxh = max(h)
ans = h.index(maxh)+1
print(ans)
