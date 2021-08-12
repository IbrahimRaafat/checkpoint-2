import math

numbers = input("Enter D: ")
numbers = numbers.split(',')

my_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    my_list.append(Q)

print(my_list)