s=input()
t=input()
if s==t:
    print('No')
    exit(0)
alp="abcdefghijklmnopqrstuvwxyz"
d={}
e={}
for i in range(len(alp)):
    d[alp[i]]=i
    e[i]=alp[i]

s_array = []
for i in range(len(s)):
    s_array.append(d[s[i]])

s_array=sorted(s_array)

t_array=[]
for j in range(len(t)):
    t_array.append(d[t[j]])

t_array=sorted(t_array,reverse=True)

s=''
for i in range(len(s_array)):
    s+=e[s_array[i]]

t=''
for j in range(len(t_array)):
    t+=e[t_array[j]]

dictionary={}
dictionary[s]=1
dictionary[t]=1

dictionary=sorted(dictionary.items(),key=lambda x: x[0])

if dictionary[0][0]==s:
    print('Yes')
else:
    print('No')