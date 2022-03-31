# создать список из кубов нечетных числе от 1 до 1000/ Вычислить сумму тех чисел из списка, сумма которых делится нацело на 7/
# к каждому элементу добавить 17 и заново вычислить сумму тех чисел, сумма которых делится нацело на 7
cubes = [x**3 for x in range(100) if x%2 != 0]
print('создан список кубов нечетных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list=[]

for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
        #вычислить сумму чисел
        my_numbers_sum = sum(my_list)
        print(my_numbers_sum)

        #сумма делится нацело на 7
        if my_numbers_sum % 7 == 0:
            print('Сумму чисел, делящихся на 7 (задание 1): ', my_numbers_sum_list )
            my_numbers_sum_list.append(my_numbers_sum)
print('Список чисел, делящихся на 7 (задание 1) : ', my_numbers_sum_list)

# добавить 17 и заново вычислить сумму тех чисел из списка, сумма которых делится нацело на 7

cubes = [(x**3)+17 for x in range(100) if x%2 == 0]
print('Создан список кубав нечетных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list_even_numbers = []

for i in range(len(cubes)):
    my_str = str(cubes)
    my_list = list(my_str)
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])
    # вычислить сумму чисел
    my_numbers_sum = sum(my_list)
    print(my_numbers_sum)
    # сумма делится нацело на 7
    if my_numbers_sum % 7 == 0:
        print('Сумму чисел, делящихся на 7 (задание 1): ', my_numbers_sum_list)
        my_numbers_sum_list_even_numbers.append(my_numbers_sum)
print('Список чисел, делящихся на 7 (задание 1) : ', my_numbers_sum_list_even_numbers)