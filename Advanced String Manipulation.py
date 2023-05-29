quote = "This is a quote."


word = quote[5:7]
print("Extracted word:", word)


upper_case = quote.upper()
lower_case = quote.lower()
title_case = quote.title()

print("Uppercase:", upper_case)
print("Lowercase:", lower_case)
print("Titlecase:", title_case)


replaced = quote.replace("quote", "sentence")
stripped = quote.strip("This ")

print("Replaced:", replaced)
print("Stripped:", stripped)


name = "Ibrahim"
formatted = "Hello, {}! Welcome.".format(name)
print("Formatted:", formatted)
