import random

def random_list_summer(n=15):
    my_list = [random.randint(-100, 100) for _ in range(n)]
    print("Generated List:", my_list)
    list_sum = sum(my_list)
    print("Sum of List:", list_sum)

random_list_summer()
