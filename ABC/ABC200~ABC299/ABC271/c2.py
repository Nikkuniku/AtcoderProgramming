n = int(input())
a = list(map(int, input().split()))

l = -1
r = n+1

while r-l > 1:
    mid = (l+r)//2
    sell = 0
    books = set([i+1 for i in range(mid)])
    c = len(books & set(a))
    if c+(n-c)//2 >= mid:
        l = mid
    else:
        r = mid

print(l)
