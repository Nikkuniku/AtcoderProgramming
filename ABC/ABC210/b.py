n=int(input())
s=input()

i=0
while True:
    if s[i]=='1':
        break
    else:
        i+=1

ans='Aoki'
if i%2==0:
    ans='Takahashi'

print(ans)