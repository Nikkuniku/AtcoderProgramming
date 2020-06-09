n,k = map(int,input().split())
seq = []
for _ in range(n):
    s = int(input())
    seq.append(s)

ans=0

right = 0
product =1

#0が含まれていれば、数列自身が最長部分列となる
if 0 in seq:
    print(n)
    exit(0)


for left in range(n):

    while right < n and product * seq[right] <=k:
        product*=seq[right]
        right+=1

    ans = max(ans , right - left)

    if left == right:
        right+=1
    else:
        product/=seq[left]


print(ans)