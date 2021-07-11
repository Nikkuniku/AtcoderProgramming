n=input()

for i in range(len(n)-1,-1,-1):
    if n[i]=='0':
        continue
    else:
        i+=1
        break

n=n[:i]

a=list(n)
b=list(reversed(n))

flg=0
for j in range(len(a)):
    if a[j]==b[j]:
        continue
    else:
        flg+=1

ans='Yes'

if flg>0:
    ans='No'

print(ans)    