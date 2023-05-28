letter = input("Enter a letter: ").lower()

if letter in 'aeiou':
    print("The letter is a vowel.")
else:
    print("The letter is a consonant.")

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("The number is divisible by 5 and 11.")
else:
    print("The number is not divisible by 5 and 11.")
