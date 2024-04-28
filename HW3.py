# 1 Привести к целому типу - 1.6, 2.99

print (int(1.6))
print (int(2.99))

# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about' 

page_name = 'www.my_site.com#about'

fixed_page_name  = page_name.replace('#', "/")

print(fixed_page_name)

# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

str = 'stroka'

str2 = ' ing'

result  =  str + str2

print(result)

            # or

str = 'stroka'

list_str =  list(str)

list_str.insert(7,' ing')

str = ''.join(list_str)

print(str)

# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

actor = 'Ivan Ivanov'

words  = actor.split()

result = words[::-1]

new_actor = ' '.join(result)

print(new_actor)

# 5 Напишите программу которая удаляет пробел в начале, в конце строки

str = "   Hello, World!   "

stripped_str = str.strip()

print(stripped_str)

# 6 Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.). 

school = {
    "1a": 22,
    "1b": 27,
    "2a": 28,
    "2b": 21,
    "3a": 24,
    "4b": 23,
    "5a": 27,
    "6b": 28,
    "7a": 21,
    "8b": 30
}

# 7 Создайте список и извлеките из него списка второй элемент.

list = ['board', "dashed", 'created']

second_el = list[1]

print(second_el)

# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment ) 

str1 = "employ"
str2 = "employment"

isIncluded = str1 in str2

if isIncluded:
    print(f'"{str1}" содержится в "{str2}"')
else:
    print(f'"{str1}" не содержится в "{str2}"')

# 9 Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt

x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])

# 10 Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

arr = [1, 5, 2, 9, 2, 9, 1]

unique_num = 0

for num in arr:
    unique_num ^= num

print(unique_num)
