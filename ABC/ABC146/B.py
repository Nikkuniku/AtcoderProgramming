N=int(input())
S=input()

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans =''
for i in range(len(S)):
    tmp_str=S[i]
    
    index = alphabet.find(tmp_str)

    rpl_str=alphabet[index+N]

    ans+=rpl_str

print(ans)