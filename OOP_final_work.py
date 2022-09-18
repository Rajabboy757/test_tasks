'''Игра морской бой'''

from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(length)]

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y,

    def move(self, go):
        if self._tp == 1:
            self._x += go
        else:
            self._y += go

    def coords(self):
        return [[i + self._x, self._y] for i in range(self._length)] if self._tp == 1 else [[self._x, self._y + i] for i
                                                                                            in range(self._length)]

    def is_collide(self, ship):

        coord = self.coords()
        coord1 = ship.coords()

        c = False

        for i in coord:
            for j in coord1:
                if i[0] == j[0] and i[1] == j[1]:
                    return True

        n = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for i in coord:
            for j in coord1:
                for k in n:
                    a = i[0] + k[0]
                    b = i[1] + k[1]
                    if a == j[0] and b == j[1]:
                        return True
        return c

    def is_out_pole(self, size):
        return not all(map(lambda x: 0 <= x[0] < size and 0 <= x[1] < size, self.coords()))

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []

    def __check(self, x):
        if self._ships.index(x) == 0:
            return True
        c = True

        for i in self._ships[:self._ships.index(x)]:
            if x.is_collide(i):
                c = False
        return c

    def init(self):
        self._ships = [Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(4, tp=randint(1, 2))
                       ]

        # rasstanovka

        for x in self._ships:
            while True:
                x.set_start_coords(randint(0, self._size - 1), randint(0, self._size - 1))
                if self.__check(x) and not x.is_out_pole(self._size):
                    break

    def get_ships(self):
        return self._ships

    def __check_move(self, x):
        c = True

        for i in self._ships:
            if x.is_collide(i):
                c = False
        return c

    def move_ships(self):
        for x in self._ships:

            if x._is_move:

                if x._tp == 1:
                    a = Ship(x._length, x._tp, x._x + 1, x._y)
                    b = Ship(x._length, x._tp, x._x - 1, x._y)
                    if self.__check_move(a) and not a.is_out_pole(self._size):
                        x.move(1)
                    elif self.__check_move(b) and not b.is_out_pole(self._size):
                        x.move(-1)
                    else:
                        continue
                else:
                    a = Ship(x._length, x._tp, x._x, x._y + 1)
                    b = Ship(x._length, x._tp, x._x, x._y - 1)

                    if self.__check_move(a) and not a.is_out_pole(self._size):
                        x.move(1)
                    elif self.__check_move(b) and not b.is_out_pole(self._size):
                        x.move(-1)
                    else:
                        continue

    def show(self):
        M = self.get_pole()
        for i in M:
            print(*i)

    def get_pole(self):
        M = [[0 for _ in range(self._size)] for _ in range(self._size)]

        for x in self._ships:
            l = x.coords()
            for i in l:
                if M[i[1]][i[0]] != 1:
                    M[i[1]][i[0]] = 1
                else:
                    print('stolknovenie')

        T = []
        for i in M:
            T.append(tuple(i))

        return tuple(T)

# a = Ship(4, 1, 0, 0)
# b = Ship(3, 2, 1, 1)
#
# print(a.is_collide(b))
# print(a.coords())
# print(b.coords())
#
# pole = GamePole(10)
# pole.init()
# pole.show()
#
#
# print()
# pole.move_ships()
# pole.show()
