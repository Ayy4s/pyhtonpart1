
name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where do you live? ")


sentence = "Hello, my name is " + name + ". I am " + age + " years old, and I live in " + city + "."
print(sentence)


upper_name = name.upper()
lower_city = city.lower()
modified_sentence = "Hello, my name is " + upper_name + ". I am " + age + " years old, and I live in " + lower_city + "."
print(modified_sentence)


name_length = len(name)
age_length = len(age)
city_length = len(city)
print("Length of name:", name_length)
print("Length of age:", age_length)
print("Length of city:", city_length)


first_name = "Ibrahim"
last_name = "Ozcan"
full_name = first_name + " " + last_name
print("Full name:", full_name)


fav_language = "Python"
language_sentence = "My favorite programming language is " + fav_language + "."
print(language_sentence)


current_year = 2023
birth_year = int(input("What year were you born? "))
age = current_year - birth_year
print("Your age is:", age)


sentence = "This is a sample sentence."
character_count = len(sentence)
print("Number of characters:", character_count)
