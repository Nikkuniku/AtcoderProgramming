N=int(input())

Lucas=[2,1]

for i in range(2,N+1):
    lucas_num = Lucas[i-1] + Lucas[i-2]
    
    Lucas.append(lucas_num)

print(Lucas)
print(Lucas[N])