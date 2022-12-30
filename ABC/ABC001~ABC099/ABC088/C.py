c1=list(map(int,input().split()))
c2=list(map(int,input().split()))
c3=list(map(int,input().split()))

c1_m=c1[0]
c2_m=c2[1]
c3_m=c3[2]

for a_1 in range(c1_m+1):
    b_1=c1_m-a_1
    
    for a_2 in range(c2_m+1):
        b_2 = c2_m-a_2

        for a_3 in range(c3_m+1):
            b_3 = c3_m-a_3

            flg=0

            if c1[0]!=(a_1+b_1):
                flg+=1
            if c1[1]!=(a_1+b_2):
                flg+=1
            if c1[2]!=(a_1+b_3):
                flg+=1
            if c2[0]!=(a_2+b_1):
                flg+=1
            if c2[1]!=(a_2+b_2):
                flg+=1
            if c2[2]!=(a_2+b_3):
                flg+=1
            if c3[0]!=(a_3+b_1):
                flg+=1
            if c3[1]!=(a_3+b_2):
                flg+=1
            if c3[2]!=(a_3+b_3):
                flg+=1
            
            if flg==0:
                print('Yes')
                exit(0)

print('No')
            


