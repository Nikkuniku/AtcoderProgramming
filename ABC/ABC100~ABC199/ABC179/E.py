from collections import defaultdict
n, x, m = map(int, input().split())
ans = 0
seen = defaultdict(int)
seen[x] = 0
arr = [x]
i = 1
looplen = 0
while True:
    x = pow(x, 2, m)
    if x in seen:
        looplen = i-seen[x]
        break
    else:
        seen[x] = i
        arr.append(x)
    i += 1
ans += sum(arr[:seen[x]])
n -= seen[x]
arr = arr[seen[x]:]
ans += sum(arr)*(n//looplen) + sum(arr[:(n % looplen)])
print(ans)
