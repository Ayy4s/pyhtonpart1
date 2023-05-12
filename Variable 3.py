# Part1
name = "Ibrahim"
age = 37
city = "Adana"

# Part2
sentence = "My name is " + name + ", I am " + str(age) + " years old, and I live in " + city + "."
print(sentence)

# Part3
title = "Mr. "
name = title + name

# Part4
sentence = "My name is {}, I am {} years old, and I live in {}.".format(name, age, city)
print(sentence)

# Part5
name = "Ibrahim"
age = 27
height = 5.8
is_student = True

# Part6
print("Type of name: {}".format(type(name)))
print(f"Type of age: {type(age)}")
print("Type of height: {}".format(type(height)))
print(f"Type of is_student: {type(is_student)}")
