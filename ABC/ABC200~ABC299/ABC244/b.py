n=int(input())
t=input()

x=0
y=0


flg=0

for i in range(n):
    if t[i]=='R':
        flg+=1
        flg%=4
    else:
        if flg==0:
            x+=1
        elif flg==1:
            y-=1
        elif flg==2:
            x-=1
        else:
            y+=1

print(x,y)