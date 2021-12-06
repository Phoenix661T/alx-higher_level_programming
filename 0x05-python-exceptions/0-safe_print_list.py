#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for j, i in enumerate(my_list):
            if j < x:
                counter = j + 1
                print("{}".format(i), end="")
        print("")
    except TypeError:
        print("No right type")
    finally:
        return counter
