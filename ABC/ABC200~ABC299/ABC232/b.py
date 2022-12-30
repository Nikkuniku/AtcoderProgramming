alphabet='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
s=input()
t=input()

def conv_alpha(x,n):
    index = alphabet.find(x)
    return alphabet[index+n]

ans='No'
for k in range(28):
    tmp=''
    for j in s:
        tmp+=conv_alpha(j,k)
    
    if tmp==t:
        ans='Yes'
        break

print(ans)