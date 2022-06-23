class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person({self.name},{self.age})'


class Cat:
    def __init__(self, nick, color):
        self.nick = nick
        self.color = color

    def price(self):
        if self.color == 'orange':
            return 100
        elif self.color == 'black':
            return 90
        else:
            return 80


class CatPerson(Cat, Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name + ' third'

    def __str__(self):
        return f'Person({self.name},{self.color})'

    def price(self):
        if self.color == 'orange':
            return 200
        elif self.color == 'black':
            return 180
        else:
            return 160

    @staticmethod
    def print_a():
        print('a')


cp = CatPerson('Gool', 'black')
print(cp.price(), cp)
