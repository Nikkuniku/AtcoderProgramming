n,x = map(int,input().split())
l = list(map(int,input().split()))

cnt =1
now = 0
for i in l:
    now += i
    if now <=x:
        cnt+=1
    else:
        print(cnt)
        exit(0)

print(cnt)
