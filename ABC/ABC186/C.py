n=int(input())

ans=0
for i in range(1,n+1):
    num10=set(str(i))
    
    num8=set(format(i,'o'))

    if '7' in num10|num8:
        continue
    else:
        ans+=1

print(ans)
