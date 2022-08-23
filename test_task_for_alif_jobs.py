class Vegs:
    def __init__(self, args):
        self.lst = args

    def add(self, *args):
        if args:
            for i in args:
                self.lst.append(i)

    def edit(self, new_value, ind=None, current_value=None):
        if ind:
            self.lst[ind] = new_value

        if current_value:
            current_value = self.__start(self.lst, current_value)
            i = self.lst.index(current_value)
            self.lst[i] = new_value

    @staticmethod
    def __start(lst, val):
        for i in lst:
            if i.startswith(val):
                return i

    def remove(self, ind=None, value=None):
        if ind:
            self.lst.pop(ind-1)  #ixdexing starts from 1

        if value:
            self.lst.remove(self.__start(self.lst, value))

    def summ(self):
        s = 0
        for i in self.lst:
            a, b = i.split('-')
            s += int(b)
        return s


def vegs_list(filename, action):
    f = open(filename, "r")
    l = []

    for i in f:
        if i.endswith('\n'):
            l.append(i[:len(i) - 1])
        else:
            l.append(i)
    f.close()

    a = Vegs(l)

    if action == 'add':
        value = input('enter value which you want to add')
        a.add(value)

    elif action == 'edit':
        current = input('enter index of value or value which you want to edit')
        new_value = input('enter your new value')

        if type(current) == int:
            a.edit(new_value, current)

        if type(current) == str:
            a.edit(new_value, None, current)

    elif action == 'remove':
        current = input('enter index of value or value which you want to edit')

        if type(current) == int:
            a.remove(current)

        if type(current) == str:
            a.remove(None, current)

    elif action == 'summ':
        print(a.summ())

    else:
        print(f'There is not {action} action in Vegs class')


    f = open(filename, "w")
    f.write('')
    f.close()

    try:
        f = open(filename, "a")
        for i in a.lst:
            f.write(str(i)+'\n')
    except:
        print("could not write to file")
    finally:
        f.close()


# for example:   vegs_list('vegs.txt', 'summ')
