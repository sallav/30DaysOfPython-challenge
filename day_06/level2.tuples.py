
fruits = ('Apple', 'Mango', 'Papaya')
vegetables = ('Tomato', 'Cucumber', 'Carrot', 'Eggplant')
animal_products = ('Meat', 'Milk', 'Cheese')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

food_stuff_tp = food_stuff_tp[:int(len(food_stuff_tp)/2)-1] + food_stuff_tp[int(len(food_stuff_tp)/2)+1:]
print(food_stuff_tp)

food_stuff_lt = food_stuff_lt[3:len(food_stuff_lt)-3]
print(food_stuff_lt)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)