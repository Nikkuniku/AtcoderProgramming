N,M=map(int,input().split())

base =['*']*N

for i in range(M):
    s_i,c_i =map(int,input().split())

    base[s_i-1]=str(c_i)

if N>=2 and base[0]=='0':
    base[0]='1' 

str_num = "".join(base)

if '*' in str_num:
    print(-1)
else:
    print(int(str_num))