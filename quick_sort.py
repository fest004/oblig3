def partition_db(l, cmp=0):
    pivot = choose_pivot(l)

    lower = []
    higher = []
    for _ in range(1, len(l)):
        cmp += 1
        if l[_] < pivot:
            lower.append(l[_])
        else:
            higher.append(l[_])

    return lower, pivot, higher, cmp

def quicksort_db(l: list, cmp=0, swap=0):
    cmp += 1
    if len(l) <= 1:
        return l, cmp, swap

    lower, pivot, higher, cmp = partition_db(l, cmp)

    sorted_lower, cmp, swap = quicksort_db(lower, cmp, swap)
    sorted_higher, cmp, swap = quicksort_db(higher, cmp, swap)

    swap += len(sorted_lower) + len(sorted_higher)

    return sorted_lower + [pivot] + sorted_higher, cmp, swap



def choose_pivot(l : list):
    return l[0]


def partition(l):
    pivot = choose_pivot(l)

    lower = []
    higher = []
    for _ in range(1, len(l)):
        if pivot < l[_]:
            higher.append(l[_])
        else:
            lower.append(l[_])

    return lower, pivot, higher


def quicksort(l : list):
    if len(l) <= 1:
        return l
    
    lower, pivot, higher = partition(l)

    return quicksort(lower) + [pivot] + quicksort(higher)





def test():
    lis = [3, 5, 1, 8, 6, 6]
    print(quicksort(lis))


test()


