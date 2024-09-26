def find_cat(cat_node : int, m : dict):
    l = [cat_node]
    n = cat_node

    while True:
        if len(m[n]) == 1:
            break
        
        for parent, children in m.items():
            if str(n) in children:
                l.append(parent)
                n = parent

    return l
        


def test():
    data = {
        25: ['24'], 
        4: ['3', '1', '2'], 
        13: ['9', '4', '11'], 
        10: ['20', '8', '7'], 
        32: ['10', '21'], 
        23: ['13', '19', '32', '22'], 
        19: ['12', '5', '14', '17', '30'], 
        14: ['6', '15', '16'], 
        30: ['18', '31', '29'], 
        24: ['23', '26'], 
        26: ['27', '28']
    }
    print(find_cat(14, data))



def inp():
    m = {}

    cat_node = int(input())

    inp = input()
    while int(inp.split(" ")[0]) != -1:
        parts = inp.split(" ")
        parent = int(parts[0])
        m[parent] = parts[1:]
        inp = input()

    print(f"cat is {cat_node}")
    print()
    print(m)
       


if __name__ == "__main__":
    #inp()
    test()
