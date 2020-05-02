S=input()

for i in range(2**3):
    sent=''+S[0]

    for j in range(3):
        if (i >> j) & 1:
            sent+='+' + S[j+1]
        else:
            sent+='-' + S[j+1]
    
    if eval(sent) == 7:
        print(sent+'=7')
        exit(0)