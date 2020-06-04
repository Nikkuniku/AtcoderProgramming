n=int(input())

total = 10**9

if n==1:
    print(0)
    exit(0)

for y in range(1,n):
    x = n/y

    if x.is_integer():
        total = min(total , abs(x - y))
    else:
        p = n%y
        x = (n-p)/y

        total = min(total , abs(x-y) + p)

print(int(total))
