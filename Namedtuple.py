from collections import namedtuple
fruit = namedtuple('brute', 'number variety color')
guava = fruit(number=2, variety='HoneyCrisp', color='green')
apple = fruit(number=5, variety='Granny Smith', color='red')

print(guava.variety)
print(guava)
print(type(guava))


