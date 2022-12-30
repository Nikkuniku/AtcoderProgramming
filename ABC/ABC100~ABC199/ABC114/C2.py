n=int(input())
cnt=0

def func(cur,use_flg,n):
    global cnt
    # ベースケース
    if cur>n:
        return
    # 3,5,7をすべて使っているならカウント
    if use_flg==0b111:
        cnt+=1

    # 7を使う
    func(cur*10+7,use_flg|0b100,n)

    func(cur*10+5,use_flg|0b010,n)

    func(cur*10+3,use_flg|0b001,n)
func(0,0,n)


print(cnt)


    