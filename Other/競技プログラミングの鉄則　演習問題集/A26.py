def isprime(p):
    div = 1
    for i in range(2, p):
        if i**2 > p:
            break
        if p % i == 0:
            div += 1

    return div == 1


q = int(input())
ans = []
for _ in range(q):
    x = int(input())
    if isprime(x):
        ans.append('Yes')
    else:
        ans.append('No')

print(*ans, sep="\n")
