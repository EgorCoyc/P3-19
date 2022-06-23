class Lab:
    i = 3
    j = 4

    def __init__(self, list_of_num):
        self._p = None
        self.list_of_num = list_of_num

    def pub_print_all(self):
        print(self.list_of_num, ' + ')
        self._print_first_el()
        self._print_second_el()
        self.__print_third_el()
        self.__print_fourth_el()
        self.__print_y()

    @staticmethod
    def print_x():
        print('x')

    @staticmethod
    def print_a():
        print('a')

    @classmethod
    def __print_y(cls):
        print('y')

    def _print_first_el(self):
        print(self.list_of_num[0])

    def _print_second_el(self):
        print(self.list_of_num[1])

    def __print_third_el(self):
        print(self.list_of_num[2])

    def __print_fourth_el(self):
        print(self.list_of_num[3])


p1 = Lab([1, 2, 3, 4, 5, 6])
p1.pub_print_all()
p1.print_x()
p1.print_a()
