n=int(input())

nodes=[1]

a=list(map(int,input().split()))

for i in range(n):
    nodes.append(pow(2,i))

nodes = list(reversed(nodes))
a=list(reversed(a))

for i in range(n):
    if i==0:
        nodes[i] = a[i]
    else:
        if (nodes[i-1] + a[i])<=pow(2,n-i):
            nodes[i] = (nodes[i-1] + a[i])
        else:
            nodes[i] = pow(2,n-i)

# print(nodes)

print(sum(nodes))