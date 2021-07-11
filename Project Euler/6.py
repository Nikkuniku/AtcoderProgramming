n=int(input())

total_sum1=0
for i in range(n+1):
    total_sum1+=i**2

total_sum2=0
for j in range(n+1):
    total_sum2+=j

total_sum2=total_sum2**2

print(total_sum2-total_sum1)