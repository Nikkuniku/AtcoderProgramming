n=int(input())

ans=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        ans=False

if ans:
    msg='{}は素数である'.format(n)
else:
    msg='{}は素数でない'.format(n)
print(msg)
