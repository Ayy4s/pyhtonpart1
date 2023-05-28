age = 20

if age < 18:
    print("You are a teenager")
else:
    print("You are an adult")
name = input("Enter your name: ")
city = "New York"

if name == "John" or name == "Jane":
    print("You are from", city)
else:
    print("You are not from", city)
password = input("Enter your password: ")

if len(password) < 6:
    print("The password is too short")
else:
    print("The password is long enough")
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
x = 5
y = 3

if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")
a = 10
b = 10

if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")
