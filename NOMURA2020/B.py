t= list(input())
n=len(t)

words = []

# for i in range(n):
#     if i==0:
#         if t[i]=='?':
#             t[i]='D'
#     else:
#         if t[i]=='?':
#             if t[i-1]=='D':
#                 t[i]='P'
#             elif t[i-1]=='P':
#                 t[i]='D'

for i in range(n):
    if i==0:
        if t[i]=='?':
            words.append('D')
        else:
            words.append(t[i])
    else:
        if t[i]=='?':
            if t[i-1]=='D':
                words.append('D')
            elif t[i-1]=='P':
                words.append('D')
            elif t[i-1]=='?':
                words.append('D')
        else:
            words.append(t[i])


ans = ''.join(t)  
ans1 = ''.join(words)


print(ans1)