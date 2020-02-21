#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
#Если строки одинаковые, вернуть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты

def comp_str(first_str, second_str):
    if type(first_str) == str and type(second_str) == str:
        if first_str == second_str:
            return 1
        elif second_str == 'learn':
            return 3
        elif len(first_str) > len(second_str):
            return 2
        elif len(first_str) < len(second_str):
            return 'Условие задачей не предусмотрено'
    else:
        return 0

print(comp_str('SomeString',0))
print(comp_str('SomeString','SomeString'))
print(comp_str('LongSomeString','SomeString'))
print(comp_str('SomeString','learn'))
print(comp_str('SomeString','LongSomeString'))