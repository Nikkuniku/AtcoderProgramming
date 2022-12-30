A,B=map(int,input().split())

cont=1
cnt=0
while cont<B:
    cont+=A-1
    cnt+=1

print(cnt)