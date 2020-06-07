s=input()
t=input()

n=len(s)

can =['a','t','c','o','d','e','r']

for i in range(n):
    if s[i] != t[i]:
        if (s[i] in can and t[i]=='@') or (s[i] =='@' and t[i] in can):
            continue
        else:
            print('You will lose')
            exit(0)


print('You can win')
        
