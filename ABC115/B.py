n=int(input())

cart =[]

for _ in range(n):
    p = int(input())

    cart.append(p)

p_m = max(cart)

index = cart.index(p_m)

total =0
for i in range(n):
    if i != index:
        total +=cart[i]
    else:
        total +=cart[i]/2

print(int(total))