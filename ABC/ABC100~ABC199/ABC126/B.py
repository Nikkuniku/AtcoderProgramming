s=input()

str_1 = s[:2]
flg_1=0
if str_1 in ['01','02','03','04','05','06','07','08','09','10','11','12']:
    flg_1=1

str_2 = s[2:]
flg_2=0
if str_2 in ['01','02','03','04','05','06','07','08','09','10','11','12']:
    flg_2=1

if flg_1==1 and flg_2==1:
    print('AMBIGUOUS')
elif flg_1==1 and flg_2==0:
    print('MMYY')
elif flg_1==0 and flg_2==1:
    print('YYMM')
else:
    print('NA')