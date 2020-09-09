#!/usr/bin/python3
def print_list_integer(my_list=[]):
    list = len(my_list)
    i = 0
    while list:
        print("{:d}".format(my_list[i]))
        list -= 1
        i += 1
