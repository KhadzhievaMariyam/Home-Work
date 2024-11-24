first = int(input('Введите чило'))
second = int(input('Введите чило'))
third = int(input('Введите чило'))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)