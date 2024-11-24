my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
positive_numbers = []
while a < len(my_list):
    number = my_list[a]
    if number > 0:
        positive_numbers.append(number)
    a += 1
    if number < 0:
       break
print(positive_numbers)
