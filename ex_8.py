# Ветвления
true_password = 'qwerty'
password = input('Введите пароль - ')

if true_password == password:
    print('Пароль верный')
    print('Доступ разрешён!')

# if true_password != password:
#     print('Пароль неверный!')
#     print('Доступ запрещён!')

else:
    print('Пароль неверный!')
    print('Доступ запрещён!')

print('конец программы')
