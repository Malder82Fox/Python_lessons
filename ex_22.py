# списки  вотличии от строк могут изменяться !!!
data = ['hello', 678, 66.9, 'tututu']
data[0] = 'теперь тут я !!!!'
# print(data[1:3])

from sys import getsizeof

# text = 'Hello'
# data_1 = 'H', 'e', 'l', 'l', 'o'
# print(getsizeof(text), getsizeof(data_1))

data.append('!!! new !!!')
a = data.pop()
print(data, a)
