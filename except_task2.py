#Перепишите функцию discounted(price, discount, max_discount=20)из урока про функции так, чтобы она 
#перехватывала исключения, когда переданы некорректные аргументы (например, строки вместо чисел).

def discounted(price, discount, max_discount=20):
    while True:
        try:
            price = abs(float(price))
            discount = abs(float(discount))
            max_discount = abs(float(max_discount))
            if max_discount > 99:
                raise ValueError('Слишком большая максимальная скидка')
            if discount >= max_discount:
                return price
            else:
                return price - (price * discount / 100)
        except ValueError:
            return 'Введен неверный формат, выполнение программы будет прервано.'

print(discounted(100, "Zero"))