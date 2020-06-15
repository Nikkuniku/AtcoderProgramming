h,w=map(int,input().split())
root=[]
for _ in range(h):
    a_i=list(input().split())

    root.append(a_i)

print(*root,sep="\n")
