N=int(input())

Restaurants =[]

for i in range(N):
    Rest,score =input().split()
    Restaurants.append([i+1,Rest,int(score)])

Restaurants.sort(key=lambda x: x[2],reverse = True)
Restaurants.sort(key=lambda x: x[1])

for j in Restaurants:
    print(j[0])