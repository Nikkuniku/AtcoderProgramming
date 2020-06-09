n,k = map(int,input().split())
seq =list(map(int,input().split()))


ans = 0
right = 0
total = 0

for left in range(n):

    while right <n and total + seq[right] < k:
        total += seq[right]
        right += 1

    ans += right - left

    if left == right:
        right += 1
    else:
        total -= seq[left]

comb = n * ( n + 1 ) / 2

print(int(comb - ans))