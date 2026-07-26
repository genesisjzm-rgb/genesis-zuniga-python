
name = 'Genesis'
age = 23
height = 5.2
is_student = True

print (name, type(name))
print (age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2
name = input('what is your name? ')
year = int(input('what year were you born '))

current_year = 2026
calc_age = current_year - year

print (f"Hi!, {name} You are approximatly, {calc_age} years old")


#Section 3

num1 = float(input("Enter a number "))
num2 = float(input("Enter another number "))

total = num1 * num2 
print (f"{num1} × {num2} = {total:.1f}")

#Section 4

Item = "Python textbook"
Price = 59.99
Quantity = 5

total = Price * Quantity

print('\n====================')
print('     RECEIPT         ')
print('====================')
print(f"Item: {Item}")
print(f"Price: ${Price:.2f}")
print(f"Quantity: {Quantity}")
print('--------------------')
print(f"Total: ${total:.2f}")
print('====================')

#Section 5
name = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("what is your favorite hobby? ")
funFact = input("What is one fun fact about yourself?")
Year = int(input("What is the year you were born?"))

Age = current_year - Year
print("\n╔════════════════════════════════════════╗")
print(f"PROFILE: {name}")
print("╠════════════════════════════════════════╣")
print(f"║ Hometown: {hometown} ║" )
print(f"║ Fun Fact: {funFact} ║")
print(f" ║Age: {Age} ║")
print("╚════════════════════════════════════════╝")

