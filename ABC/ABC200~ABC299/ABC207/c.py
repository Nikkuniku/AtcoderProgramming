n=int(input())
seg=[]
for _ in range(n):
    seg.append(list(map(int,input().split())))

ans=0
for i in range(n):
    for j in range(i+1,n):
        p=seg[i]
        q=seg[j]

        seg_flg_p = p[0]
        seg_flg_q = q[0]
        a=p[1]
        b=p[2]
        c=q[1]
        d=q[2]
        
        if seg_flg_p==1:
            if seg_flg_q==1:
                if a<=d and c<=b:
                    ans+=1
            elif seg_flg_q==2:
                if a<d and c<=b:
                    ans+=1
            elif seg_flg_q==3:
                if a<=d and c<b:
                    ans+=1
            else:
                if a<d and c<b:
                    ans+=1
        elif seg_flg_p==2:
            if seg_flg_q==1:
                if a<=d and c<b:
                    ans+=1
            # elif seg_flg_q==2:
            #     if a<d and c<b:
            #         ans+=1
            elif seg_flg_q==3:
                if a<=d and c<b:
                    ans+=1
            else:
                if a<d and c<b:
                    ans+=1
        elif seg_flg_p==3:
            if seg_flg_q==1:
                if a<d and c<=b:
                    ans+=1
            elif seg_flg_q==2:
                if a<d and c<=b:
                    ans+=1
            # elif seg_flg_q==3:
            #     if a<d and c<b:
            #         ans+=1
            else:
                if a<d and c<b:
                    ans+=1
        else:
            if a<d and c<b:
                ans+=1            

print(ans)