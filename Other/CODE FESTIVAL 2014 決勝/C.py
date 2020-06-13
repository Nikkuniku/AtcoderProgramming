a= int(input())

for k in range(10,10001):
    ans=a

    
    s_k = str(k)
    l_k = list(s_k)
    n_k = len(l_k)

    for i in range(n_k):
        ans-=int(l_k[i])*(k**(n_k-1-i))

    
    if ans==0:
        print(k)
        exit(0)

print(-1)
