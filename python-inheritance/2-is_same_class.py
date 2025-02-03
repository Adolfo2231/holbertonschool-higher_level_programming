def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class  # ✅ Usamos `is` en lugar de `==`
