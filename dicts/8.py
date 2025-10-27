n = int(input())
city_to_country = {}

for i in range(n):
    data = input().split()
    country = data[0]
    cities = data[1:]
    for city in cities:
        city_to_country[city] = country

m = int(input())

for i in range(m):
    city = input().strip()
    print(city_to_country[city])
