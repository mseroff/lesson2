#Перепишите функцию discounted(price, discount, max_discount=20)из урока про функции так, чтобы она 
#перехватывала исключения, когда переданы некорректные аргументы (например, строки вместо чисел).

def discounted(price, discount, max_discount=20): 
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
    except ValueError:
        return 'Введен неверный формат, выполнение программы будет прервано.'
    if max_discount > 99:
        return 'Слишком большая максимальная скидка'
    elif discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)


print(discounted(100, 'Zero'))