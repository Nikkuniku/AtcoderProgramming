N=int(input())
if N==1:
    exit(print(1))
divs=[0]*(N+1)
for i in range(1,N+1):
    j=i
    cnt=0
    while j%2==0:
        cnt+=1
        j//=2
    divs[i]=cnt
print(divs.index(max(divs)))