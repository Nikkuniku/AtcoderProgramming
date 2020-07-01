s=input()


from collections import Counter

c=Counter(s)
if len(list(c.keys()))==1:
    print(0)
    exit(0)


cnt=101
targets=list(c.keys())

for t in targets:
    tmp_cnt=0
    prev=s
    minus=1
    while True:
        tmp=''
        tmp_cnt+=1
        for i in range(len(s)-minus):
            if prev[i]==t or prev[i+1]==t:
                tmp+=t
            else:
                tmp+=prev[i]

        tmp_c=Counter(tmp)
        if len(list(tmp_c.keys()))==1:
            break
        else:
            minus+=1
            prev=tmp

    cnt=min(cnt,tmp_cnt)

print(cnt)