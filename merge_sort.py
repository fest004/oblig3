#Implement merge sort

def merge_sort_db(l: list, cmp=0, swap=0):
    # Base case
    if len(l) == 1:
        return l, cmp, swap

    mid = len(l) // 2

    left = l[:mid]
    right = l[mid:]

    # Recursively split and sort the lists
    left, cmp, swap = merge_sort_db(left, cmp, move)
    right, cmp, swap = merge_sort_db(right, cmp, move)

    i = j = k = 0

    # Merging the two lists
    while i < len(left) and j < len(right):
        cmp += 1  # Counting the comparison in the merge
        if left[i] < right[j]:
            l[k] = left[i]
            i += 1
        else:
            l[k] = right[j]
            j += 1
        k += 1
        swap += 1  # Counting the move (placing the value in l[k])

    # Copy the remaining elements of left[], if any
    while i < len(left):
        l[k] = left[i]
        i += 1
        k += 1
        swap += 1  # Counting the move

    # Copy the remaining elements of right[], if any
    while j < len(right):
        l[k] = right[j]
        j += 1
        k += 1
        swap += 1  # Counting the move

    return l, cmp, swap






def merge_sort(l : list):
    # Base case
    if len(l) == 1:
        return l

    mid = len(l) // 2

    left = l[mid:]
    right = l[:mid]


    merge_sort(left)
    merge_sort(right)


    i = j = k = 0

    # Merging the two lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l[k] = left[i]
            i += 1
        else: 
            l[k] = right[j]
            j += 1
        k += 1

    #if there are more elements in either array respectively
    while i < len(left):
        l[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        l[k] = right[j]
        j += 1
        k += 1

    return l 
        


def test():
    l = [38, 27, 43, 3, 9, 82, 10]
    l = merge_sort(l)
    print(l)



test()
