def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Create a string for the current row
        row_string = ""
        for i, num in enumerate(row):
            # Append the formatted number to the row string
            row_string += "{}".format(num)
            # Add a space after each number except the last one
            if i < len(row) - 1:
                row_string += " "
        # Print the row string
        print(row_string)
