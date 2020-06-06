l,x,y,s,d = map(int,input().split())

h = l/2
if d==0:
    d=l

# if s<h:
#     if s<=d and d<=s+h:
#         d1 =abs(d-s)
#         d2 = l - d1 
#     else:
#         if s+h<d and d<=l:
#             d1 = abs(s-d)
#             d2 = l-d1
#         else:
#             d2 = abs(s-d)
#             d1 = l-d2 
# elif s>h:
#     border = s-h
#     if border<=d and d<=s:
#         d2 = abs(d-s)
#         d1 = l-d2
#     else:
#         if s<d and d<=l:
#             d1 = abs(d-s)
#             d2 = l-d1
#         else:
#             d2 = abs(d-s)
#             d1 = l-d2
# else:
#     if d<=s:
#         d2 = abs(d-s)
#         d1 = l-d2
#     else:
#         d1 = abs(d-s)
#         d2 = l-d1

# #時計回りの時間
# t1 = d1/(x+y)

# if y-x!=0:
#     #反時計回りの時間
#     t2 = d2/(y-x)
# else:
#     t2=10**9
# if t2<0:
#     t2=10**9

# print(min(t1,t2))


if s<=d:
    d1 = d-s
    d2 = l-d1
else:
    d1 = l-s +d
    d2 = l-d1

if x<y:
    t1 = d1 / (x+y)
    t2 = d2 / (y-x)
else:
    t1 = d1 / (x+y)
    t2 = 10**9

print(min(t1,t2))
