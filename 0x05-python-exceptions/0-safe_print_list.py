#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        printed_list_elements = 0
        for i in range(x):
            print(my_list[i], end="")
            printed_list_elements += 1
        print()
        return printed_list_elements

    except IndexError:
        print()
        return printed_list_elements
