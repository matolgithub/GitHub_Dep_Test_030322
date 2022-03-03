food_1 = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис', 'Мясо']
prod = input().lower()
food_2 = []
for item in food_1:
    food_2.append(item.lower())
#print(food_2, prod)
if prod not in food_2:
    print("Do not this product in list!")
else:
    while prod in food_2:
        food_2.remove(prod)
    print(food_2)