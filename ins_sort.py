#Implement insertion sort


def insert_sort_db(l : list):
    i = 1
    cmp = swap = 0

    while i < len(l):
        cmp += 2
        if l[i] < l[i-1]:
            # Swapping elements
            tmp = l[i]
            l[i] = l[i - 1]
            l[i-1] = tmp

            cmp += 1
            if i > 1:
                i -= 1
        else: 
            i += 1

    return l, cmp, swap




def insert_sort(l : list):
    i = 1

    while i < len(l):
        print(l)
        if l[i] < l[i-1]:
            # Swapping elements
            tmp = l[i]
            l[i] = l[i - 1]
            l[i-1] = tmp

            if i > 1:
                i -= 1
        else: 
            i += 1

    return l

def test():
    l = [10, 5, 2, 5, 8, 3, 1]
    l = insert_sort(l)
    print(l)



if __name__ == "__main__":
    #inp()
    test()
