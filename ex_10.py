# Форматирование

name = input('Введите Ваше имя - ')
age = input ('Введите Ваш возраст - ')
# print('Вас зовут - ', name, 'Ваш возраст - ', age)
# print('Вас зовут - {}, Ваш возраст - {}'.format(name, age))
print(f'Вас зовут - {name}, Ваш возраст - {age}')

number = float(input('Введите число (дробь с 5-ю знаками поле запятой) - '))
print(f'Ваше число - {number:.3fa}')

text = 'Hello ' \
       'World'
print(text)
