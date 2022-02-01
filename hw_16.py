i = float(input('How long did you run on the first day, km? - '))
b = int(input('What is your training day? - '))

while b != 1:
    b = b - 1
    i = i * 1.1
print('You have to run -', round(i, 2))
