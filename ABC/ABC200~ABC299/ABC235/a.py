s=list(input())

a=s
b=s[1:]+s[:1]
c=s[2:]+s[:2]
a=int(''.join(a))
b=int(''.join(b))
c=int(''.join(c))
ans=a+b+c
print(ans)