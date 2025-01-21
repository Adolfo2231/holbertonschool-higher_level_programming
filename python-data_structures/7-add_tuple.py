def add_tuple(tuple_a=(), tuple_b=()):
    # Get the first two elements of each tuple, defaulting to 0 if not present
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    # Return a new tuple with the sums of the corresponding elements
    return (a1 + b1, a2 + b2)
