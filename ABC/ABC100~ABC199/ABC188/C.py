n=int(input())
a=list(map(int,input().split()))

# tmp=a
# for i in range(n):

#     result=[]
    
#     for j in range(2**(n-(i+1))):
#         l=tmp[2*j]
#         r=tmp[2*j + 1]

#         if l>r:
#             result.append(l)
#         else:
#             result.append(r)
    
#     tmp=result

#     if len(result)==2:
#         break

# second=min(result)
# print(a.index(second)+1)

a_l=a[:len(a)//2]
a_r=a[len(a)//2:]

m_l=max(a_l)
m_r=max(a_r)

ans=0
if m_l>m_r:
    ans=a.index(m_r)
else:
    ans=a.index(m_l)
ans+=1

print(ans)

