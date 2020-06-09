    n,m =map(int,input().split())

    foods =set([ i+1 for i in range(m)])


    for _ in range(n):
        k = list(map(int,input().split()))
        fav = set(k[1:])

        foods = foods&fav

    if len(foods)!=0:
        print(len(foods))
    else:
        print(0)