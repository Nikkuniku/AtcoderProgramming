n = int(input())
w=list(map(int,input().split()))

dist =10**18
for i in range(1,n):
    a= w[:i]
    b= w[i:]

    a_sum = sum(a)
    b_sum = sum(b)

    dist = min (dist , abs(a_sum - b_sum))


print(dist)