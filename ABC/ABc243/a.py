v,a,b,c=map(int,input().split())

i=0
while True:
    if i==0:
       if v<a:
           ans='F'
           break
       else:
            v-=a
            i+=1
    elif i==1:
        if v<b:
            ans='M'
            break
        else:
            v-=b
            i+=1
    else:
        if v<c:
            ans='T'
            break
        else:
            v-=c
            i=0
print(ans)
