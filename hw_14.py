a = int(input('Enter Your number: '))
b = a // 10
c = b // 10
d = c // 10
e = d // 10
f = e // 10
g = f // 10
h = g // 10
i = h // 10

a_1 = i // 10
a_2 = i % 10
a_3 = h // 10
a_4 = g // 10
a_5 = f // 10
a_6 = e // 10
a_7 = d // 10
a_8 = c // 10
a_9 = b // 10
a_0 = a // 10

num = [a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_0]

print('Max digit in this number - it is: ', max(num))
print(a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_0)
