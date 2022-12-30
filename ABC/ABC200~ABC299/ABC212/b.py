s=list(input())

nums=set(s)
ans='Strong'
if len(nums)==1:
    ans='Weak'

d={"0":"1"
,"1":"2"
,"2":"3"
,"3":"4"
,"4":"5"
,"5":"6"
,"6":"7"
,"7":"8"
,"8":"9"
,"9":"0"}

flg=0
for i in range(len(s)-1):
    if d[s[i]]==s[i+1]:
        flg+=1

if flg==3:
    ans='Weak'


print(ans)