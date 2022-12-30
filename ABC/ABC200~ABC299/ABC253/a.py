a, b, c = map(int, input().split())
arr = [a, b, c]
arr.sort()
if arr[1] == b:
    print('Yes')
else:
    print('No')
