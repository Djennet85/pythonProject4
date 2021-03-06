# Программа принимает действительное положительное число x и целое отрицательное
# число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.


def my_func(x, y):
    result = x ** y
    return result


result = my_func(5, -2)
print(f"Sub: {result}")

def my_func2(x, y):
    x, y = float(x), int(y)
    if x <= 0 or y >= 0:
        return "Не выполненно условие ввода данных:\nx должен быть больше 0 \ny должен быть меньше 0"
    else:
        result = 1
        for _ in range(abs(y)):
            result /= x
        return f"Результат возведения x в степень y: {round(result, 4)}"

number_1 = input("Введите положительное число, x = ")
number_2 = input("Введите целое отрицательное число, y = ")

print(my_func2(number_1, number_2))