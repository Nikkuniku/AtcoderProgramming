def judge(a, b):
    l = -1
    r = b-a
    while r-l > 1:
        mid = (l+r)//2


# T=int(input())
# for _ in range(T):
#     A,B=map(int,input().split())
a, b = map(int, input().split())
print(judge(a, b))
