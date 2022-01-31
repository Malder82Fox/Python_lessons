password = 'qwerty'

max_mistakes = 3
current_attempt = 1

# user_password = input('Enter password: ')
# while password != user_password or current_attempt <= max_mistakes:
#     current_attempt += 1 # current_attempt = current_attempt + 1
#     last_attemp = max_mistakes - current_attempt
#     print(f'Password not correct ! Try again ! Attempts left: {last_attemp} ')

while True:
    user_password = input('Enter password: ')

    if user_password == password:
        print('Access !')
        break

    if current_attempt >= max_mistakes:
        print('!!! Attention. Account is blocked !!!')
        break

    last_attemp = max_mistakes - current_attempt
    print(f'Password not correct ! Try again ! Attempts left: {last_attemp} ')
    current_attempt += 1

