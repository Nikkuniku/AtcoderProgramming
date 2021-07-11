l,r=map(int,input().split())
mod=10**9 + 7

def cnt(x):
    i=0
    ans=0
    while True:
        if x/pow(10,i)<10:
            ans+= (i+1)*(x*(x+1) -pow(10,i)*(pow(10,i)-1))//2 
            break
        else:
            ans+= (i+1)*pow(10,i)*( 10*(pow(10,i+1)-1) - pow(10,i) + 1 )//2 
            i+=1

    return ans

answer = cnt(r)-cnt(l-1)
print(answer%mod)

