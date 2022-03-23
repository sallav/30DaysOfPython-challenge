
score = int(input("Enter your score: "))

if score>80:
    print("Your grade: A")
elif score>70 and score<89:
    print("Your grade: B")
elif score>60 and score<69: 
    print("Your grade: C")
elif score>50 and score<59: 
    print("Your grade: D")
else:
    print("Your grade: F")

month = input("Enter the month: ")

if month.startswith('September') or month.startswith('October') or month.startswith('November'):
    print("It's autumn.")
elif month.startswith('December') or month.startswith('January') or month.startswith('February'):
    print("It's winter.")
elif month.startswith('March') or month.startswith('April') or month.startswith('May'):
    print("It's spring.")
elif month.startswith('June') or month.startswith('July') or month.startswith('August'):
    print("It's summer.")
else:
    print("That is not a month!") 
       
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print("Fruits: " + ', '.join(fruits))