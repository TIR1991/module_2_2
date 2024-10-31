first = int(input('Введите число %1'))
second = int(input('Введите число %2'))
third = int(input('Введите число %3'))
if first==second==third:
    print(3)
elif first == second:
    print(2)
elif first == third:
    print(2)
elif second == third:
    print(2)
else:
    print("Совпадений нет")