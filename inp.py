# default libs
import sys
import time 

# my files
import ins_sort as ins
import merge_sort as merge_s
import quick_sort as qs
#import bogo_sort as bs #Fitting


def write_csv(name, data):
    with open(name, "a") as f:
        for i in range(0, len(data) - 1):
            f.write(f"{data[i]}, ")
        f.write(f"{data[-1]} \n")
    f.close()


def write_sort_res(name: str, l: list):
    with open(name, "w") as f:
        for element in l:
            f.write(f"{element}")  

def read_from_file(name : str) -> list:
    with open(name, "r") as f:
        input_arr = [int(line.strip()) for line in f.readlines()]
    f.close()
    return input_arr


#

def inp_from_file(filepath : str):

    #constant
    INPUT_ARR = read_from_file(filepath)

    for i in range(1, len(INPUT_ARR) - 1):
        data = []
        data.append(i)

        input_arr = INPUT_ARR[:i]

        t_0 = time.time_ns()
        res = ins.insert_sort_db(input_arr)
        t_1 = time.time_ns()
        dt = (t_1 - t_0) / 1000
        write_sort_res("results/insert_sort.txt", res[0])
        data.append(res[1])
        data.append(res[2])
        data.append(dt)

        t_0 = time.time_ns()
        res = merge_s.merge_sort_db(input_arr)
        t_1 = time.time_ns()
        dt = t_1 - t_0 / 1000
        write_sort_res("results/merge_sort.txt", res[0])
        data.append(res[1])
        data.append(res[2])
        data.append(dt)



        t_0 = time.time_ns()
        res = merge_s.quicksort_db(input_arr)
        t_1 = time.time_ns()
        dt = t_1 - t_0 / 1000
        write_sort_res("results/quick_sort.txt", res[0])
        data.append(res[1])
        data.append(res[2])
        data.append(dt)


        #t_0 = time.time.ns()
        #res = bs.bogosort(input_arr)
        #t_1 = time.time.ns()
        #bs_dt = t_1 - t_0
        #write_sort_res("results/bogo_sort.txt", res[0])
        #data.append[1]
        #data.append[2]

        write_csv(f"{filepath}_results.csv", data)




if __name__ == "__main__":
    file = sys.argv[1]
    inp_from_file(file)

