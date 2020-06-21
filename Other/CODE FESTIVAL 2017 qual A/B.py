n,m,k=map(int,input().split())

can=[]
for i in range(n+1):
    for j in range(m+1):
        can.append(n*j+i*m - 2*i*j)


# can_m=[]
# can_n=[]

# for i in range(m+1):
#     can_m.append(i*n)
# for i in range(m+1):
#     p = can_m[i]
#     for j in range(1,m):
#         s = i*n - i*j + j*(m-i)
#         can_m.append(s)

# for i in range(n+1):
#     can_n.append(i*m)
# for i in range(n+1):
#     p = can_n[i]
#     for j in range(1,n):
#         s = i*m - i*j + j*(n-i)
#         can_n.append(s)

if (k in can): #or (k in can_n):
    print('Yes')
else:
    print('No')