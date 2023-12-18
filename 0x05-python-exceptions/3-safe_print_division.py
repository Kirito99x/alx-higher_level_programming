#!/usr/bin/python3

def safe_print_division(a, b):
    divi = None
    try:
        divi = a / b
    except (TypeError,  ValueError, ZeroDivisionError):
        divi = None
    finally:
        print("Inside result: {}".format(divi))
    return (divi)
