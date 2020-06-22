s=input()
t=input()


kouho=[]
for i in range(len(s)-len(t)+1):
    ans=s[:i]
    tmp=s[i:(i+len(t))]

    for j in range(len(t)):
        if tmp[j]==t[j]:
            ans+=t[j]
        elif tmp[j]=='?': 
            ans+=t[j]
        elif tmp[j]!='?' and tmp[j]!=t[j]:
            break
    ans=ans+s[(i+len(t)):]

    if len(ans)==len(s):
        kouho.append(ans)

if len(kouho)==0:
    print('UNRESTORABLE')
    exit(0)

answers=[]
for j in kouho:

    tmp_ans=''
    for k in range(len(j)):
        if j[k]=='?':
            tmp_ans+='a'
        else:
            tmp_ans+=j[k]

    answers.append(tmp_ans)

answers=sorted(answers)
print(answers[0])




