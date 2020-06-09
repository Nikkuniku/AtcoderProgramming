N=int(input())

numbers = []

for i in range(1,9+1):
    for j in range(1,9+1):
        numbers.append(i*j)

if N in numbers:
    print('Yes')
else:
    print('No')