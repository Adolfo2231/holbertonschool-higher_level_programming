#!/usr/bin/env python3

if __name__ == "__main__":
    # Import add function from add_0.py
    from add_0 import add

    # Define the values of a and b
    a = 1
    b = 2

    # Call the add function and print the formatted result
    print(f"{a} + {b} = {add(a, b)}")
