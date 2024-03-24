# Создайте функцию генератор чисел Фибоначчи https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%
# 81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

a = int(input('Введите целое число: '))


def fibonacci(n):
    fn = [0, 1]
    for i in range(2, n):
        fn.append(fn[i-1] + fn[i-2])
    return fn


print(fibonacci(a))

