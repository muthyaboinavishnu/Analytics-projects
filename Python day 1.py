#Strings
#concat


print("Hello! " + input("what is our name?"))

name = input("What is your name?")
length = len(name)
print(name+":"+length)

# Day 2:-

num_char = len(input("What is your name?\n"))
print("Your name has " + "letters")

# BMI calculation

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / height**2
print(int(BMI))

### Tip calculator program
print('Welcome to the tip claculator')
bill = float(input("Enter total bill amount\n"))
tip_precent = float(input('What percentage of tip you would like to give?\n'))
tipped_total = (tip_precent/100 + 1)*bill

persons = int(input("How many persons are splitting?\n"))
#bill_each = round((tipped_total / persons),2)
bill_each = "{:.2f}".format(tipped_total / persons)
print(f"Each person should pay {bill_each}")

