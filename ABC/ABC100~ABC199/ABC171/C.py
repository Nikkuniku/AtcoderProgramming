n=int(input())

# alp='abcdefghijklmnopqrstuvwxyz'

# ########関数部分##############
# def Base_10_to_n(X, n):
#     if (int(X/n)):
#         return Base_10_to_n(int(X/n), n)+' '+str(X%n)
#     return str(X%n)
# ############################
# l=list(Base_10_to_n(n,26).split())
# print(l)
# ans=''

# for i in range(len(l)):
#     ans+=alp[int(l[i])-1]

# 数値→アルファベット
def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)
ans=num2alpha(n).lower()

print(ans)