from itertools import groupby
n = int(input())
a = list(map(int, input().split()))
g = groupby(a)
arr = []
for key,group in g:
    arr.append(key)
diff = []
m = len(arr)
if m > 1:
    for i in range(m-1):
        diff.append(arr[i+1]-arr[i])

    index = -1
    for k in range(len(diff)):
        if diff[k] < 0:
            index = k
            break
    erase = arr[index]
else:
    erase = arr[0]

ans = []
for c in a:
    if c != erase:
        ans.append(c)
print(*ans)
