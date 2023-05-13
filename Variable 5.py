name = input("Enter your name: ")
first_character = name[0]
last_character = name[-1]
print("First character:", first_character)
print("Last character:", last_character)


if any(char.isdigit() for char in name):
    print("The name contains digits.")
else:
    print("The name does not contain any digits.")


sentence = "Hello [name], how are you today?"
new_sentence = sentence.replace("[name]", name)
print("New sentence:", new_sentence)


words = sentence.split()
for word in words:
    print(word)