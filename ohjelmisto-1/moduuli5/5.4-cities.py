# Kaupunkeja

city_list = []
print("Enter five city names. One per line")
for _ in range(5):
    city_list.append(input("> "))

for city in city_list:
    print(city)
