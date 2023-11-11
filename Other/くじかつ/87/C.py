s=input()
t=input()

s_d = ''.join(sorted(s))
t_d = ''.join(sorted(t,reverse=True))

arr = [t_d,s_d]
arr=sorted(arr)

if s==t:
    print('No')
    exit(0)

if arr[0]==s_d:
    print('Yes')
else:
    print('No')