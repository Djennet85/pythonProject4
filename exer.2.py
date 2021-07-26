#Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def personal_info(**kwargs):
    return ' '.join(kwargs.values())

print(personal_info(name=input("Введите имя: "),soname=input("Введите фамилию: "),
                    age =input("Введите год рождения: "), city=input("Введите город проживания: "),
                    email = input("Введите вашу почту: "),phone_number = input("Введите ваш номер телефона: ")))


int_func = lambda word: word.title() if word.islower() and ascii(word)[1:-1].isalpha() else''
print('_'.join(map(int_func, input("Введите фразу: ").split())))
