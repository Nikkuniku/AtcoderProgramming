n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sum_a=sum(a)
sum_b=sum(b)

cumsum=0
cnt=0
i=0
j=0
while True:
    if i<=n-1:
        a_i=a[i]
    else:
        a_i=10**9+1
    
    if j<=m-1:
        b_j=b[j]
    else:
        b_j=10**9 + 1

    if a_i < b_j:
        cumsum+=a_i
        sum_a-=a_i
        i+=1
    elif a_i > b_j:
        cumsum+=b_j
        sum_b-=b_j
        j+=1
    elif a_i==b_j:
        if sum_a<=sum_b:
            cumsum+=a_i
            sum_a-=a_i
            i+=1
        else:
            cumsum+=b_j
            sum_b-=b_j
            j+=1
    
    if cumsum<=k:
        cnt+=1
    else:
        break

    if i>n-1 and j>m-1:
        break

print(cnt)