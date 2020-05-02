products=(("みかん",100),("リンゴ",200),("ブドウ",300))
N=len(products)

for i in range(2**N):
    Bug=[]
    items=[]
    for j in range(N):
        if (i>>j) & 1 :
            Bug.append(products[j][1])
            items.append(products[j][0])

    if sum(Bug)>300:
        continue
    print(Bug)
    print(items)


