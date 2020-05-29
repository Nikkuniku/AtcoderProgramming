n=int(input())

total =0
btc=0
for _ in range(n):
    x,u = input().split()

    x= float(x)

    if u=='JPY':
        total+=x
    else:
        btc+=x

total += btc*380000

print(total)