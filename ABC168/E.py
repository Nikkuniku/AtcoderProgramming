n = int(input())

fish={}

fish_2 = {}
for _ in range(n):
    a,b =map(int,input().split())

    v_i = a/b
    v_j = b/a

    if v_i not in fish:
        fish[v_i]=1
    else:
        fish[v_i]+=1

    if v_i not in fish_2:
        fish_2[v_j]=1
    else:
        fish_2[v_j]+=1
    

    
