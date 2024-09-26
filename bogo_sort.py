import random


def is_sorted(l : list):
    for _ in range(len(l) - 1):
        if l[_] > l[_+1]:
            print("Failed")
            return False
    print("Success")
    return True


def bogosort(l : list):
    while is_sorted(l) == False:
        random.shuffle(l)
    return l




def test():
    l_2 = [2, 4, 15, 16, 17]
    bogosort(l_2)


test()



