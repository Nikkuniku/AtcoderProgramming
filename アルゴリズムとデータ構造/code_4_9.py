def func(i,w,a):
    if i==0:
        if w==0:
            return True
        else :
            return False

    # a_i-1を選ばない
    if func(i-1,w,a)==True:
        return True

    # a_i-1を選ぶ
    if func(i-1,w-a[i-1],a)==True:
        return True

    return False

n=int(input())
w=int(input())
a=list(map(int,input().split()))


print(func(n,w,a))