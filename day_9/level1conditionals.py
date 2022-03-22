
age = int(input("Enter your age: "))

if age>=18:
    print("You are old enough to drive.")
else:
    years_to_drive = 18-age
    print("You need {} more years to learn to drive".format(years_to_drive))

my_age = 40
your_age = int(input("Enter your age: "))

if my_age<your_age:
    if (your_age-my_age)>1:
        print("You are " + str(your_age-my_age) + " years older than me")
    else:
        print("You are one year older than me")
elif my_age==your_age:
    print("We are the same age!")
else:
    if (my_age-your_age)>1:
        print("You are " + str(my_age-your_age) + " years younger than me")
    else:
        print("You are one year younger than me")
        
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a<b:
    print("{} is greater than {}".format(b, a))
elif a>b:
    print("{} is less than {}".format(b, a))
else:
    print("{} and {} are equal numbers".format(a, b))
