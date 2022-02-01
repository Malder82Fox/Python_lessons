num_1 = int(input('What profit to Your a Company, USD - '))
num_2 = int(input('What expenses to Your a Company, USD - '))

if num_2 == 0:
    print('Your profit', num_1, 'USD')
    print('!!! You have to pay taxes )))) !!!')

elif num_1 > num_2:
    print('Your profit ', num_1 - num_2, 'USD')
    print('Your company is profitability ', round(num_1 / num_2, 2))
    num_3 = int(input('How many employees do you have? - '))
    print('Your Profit per Person - ', round(num_1 / num_3, 2))

elif num_1 == num_2:
    print('Your profit ', num_1 - num_2, 'USD')
    print('Could be worse')

elif num_1 < num_2:
    print('Your expenses ', num_1 - num_2, 'USD')
    print('You loser')
