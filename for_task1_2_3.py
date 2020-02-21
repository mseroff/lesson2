#Задание 1
#Цикл
#Создать список из десяти целых чисел.
#Вывести на экран каждое число, увеличенное на 1.
print('Задание 1:')

list_of_numbers = [16,5,2,9,45]

for i in list_of_numbers:
    print(i+1)

#Задание 2
#Цикл
#Ввести с клавиатуры строку.
#Вывести эту же строку вертикально: по одному символу на строку консоли.
print('Задание 2:')

my_string = input('Введите любую строку\n')

for i in my_string:
    print(i)

#Задание 3
#Оценки
#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.
print('Задание 3:')

marks = [
        {'school_class': '10A', 'scores': [3,3,5,3,5]},
        {'school_class': '10B', 'scores': [2,2,5,3,1]},
        {'school_class': '9A', 'scores': [4,3,3,3,4]},
        {'school_class': '9B', 'scores': [4,5,5,4,5]}
]

all_marks_of_school = 0
count = 0
for i in marks:
    all_marks_of_school += sum(i['scores'])
    count += len(i['scores'])
    print('Средний бал учащихся по классу {}: {}'.format(i['school_class'], (sum(i['scores'])/len(i['scores']))))
print('Средний учащихся бал по школе: {}'.format(all_marks_of_school/count))



