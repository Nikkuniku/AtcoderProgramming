x,y=map(int,input().split())

#i:亀
#j:鶴
cnt=0
for i in range(x+1):
    j = x-i

    cnt = i*4 + j*2

    if cnt==y:
        print('Yes')
        exit(0)

print('No')
