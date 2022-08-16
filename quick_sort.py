from random import randrange

def qsort(lst):
    if len(lst) < 2:
        return lst

    else:

        pivot = lst.pop(randrange(len(lst)))
        small = [i for i in lst if i <= pivot]
        big = [i for i in lst if i > pivot]
        return qsort(small) + [pivot] + qsort(big)


lst = [3, 6, 5, 8, 11, 10, 13, 1, 22, 2, -1, 5, 7, 9]
print(qsort(lst))