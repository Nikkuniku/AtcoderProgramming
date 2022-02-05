s=input()

ans=''
if len(s)>=3:
    a=s[-3:]
    if a=='ist':
        ans='ist'
b=s[-2:]
if b=='er':
    ans='er'

print(ans)
