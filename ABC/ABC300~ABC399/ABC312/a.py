S = input()
A = 'ACE,BDF,CEG,DFA,EGB,FAC,GBD'.split(',')
ans = 'No'
if S in A:
    ans = 'Yes'
print(ans)
