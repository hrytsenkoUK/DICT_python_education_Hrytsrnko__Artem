def read_matrix():
    """
        Reads a matrix from user input.
        This function prompts the user to enter the dimensions of a matrix and its
        elements, and then creates and returns the matrix as a list of lists.

        Args:
            None

        Returns:
            list: A 2D list representing the entered matrix, where each inner list
                  corresponds to a row of the matrix.
    """
    n, m = map(int, input("Enter size of matrix: ").split())
    matrix = []
    print("Enter matrix:")
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix


def add_matrices():
    """
    Adds two matrices entered by the user.
    This function prompts the user to enter the size and elements of two matrices.
    It then checks if the matrices have the same dimensions. If the dimensions are
    incompatible, it prints an error message and exits. Otherwise, it performs element-wise
    addition of the matrices and prints the resulting matrix.

    Args:
        None

    Returns:
        None
    """
    matrix_a = read_matrix()
    matrix_b = read_matrix()

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("The operation cannot be performed.")
        return

    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)

    print("The result is:")
    for row in result:
        print(*row)


def multiply_matrix_by_constant():
    """
        Multiplies a matrix entered by the user by a constant value.
        This function prompts the user to enter the size and elements of a matrix,
        and then asks for a constant value. It performs element-wise multiplication
        between the matrix elements and the constant, and returns the resulting matrix.

        Args:
            None

        Returns:
            None
    """
    matrix = read_matrix()
    constant = float(input("Enter constant: "))

    result = []
    for row in matrix:
        new_row = [element * constant for element in row]
        result.append(new_row)

    print("The result is:")
    for row in result:
        print(*row)


def multiply_matrices():
    """
        Multiplies two matrices entered by the user.
        This function prompts the user to enter the size and elements of two matrices.
        It performs matrix multiplication, which requires the number of columns in the
        first matrix (inner dimension) to be equal to the number of rows in the second
        matrix. If this condition is not met, the function prints an error message and exits.
        Otherwise, it calculates the resulting product matrix and prints it.

        Args:
            None

        Returns:
            None
    """
    matrix_a = read_matrix()
    matrix_b = read_matrix()

    if len(matrix_a[0]) != len(matrix_b):
        print("The operation cannot be performed.")
        return

    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            element_sum = 0
            for k in range(len(matrix_b)):
                element_sum += matrix_a[i][k] * matrix_b[k][j]
            row.append(element_sum)
        result.append(row)

    print("The result is:")
    for row in result:
        print(*row)


def transpose_matrix():
    """
        Transposes a matrix entered by the user based on user choice.
        This function offers four options for transposing a matrix:
        1. Main diagonal: Swaps rows and columns, reflecting along the main diagonal.
        2. Side diagonal: Swaps rows and columns, reflecting along the opposite diagonal.
        3. Vertical line: Flips each row to reverse the order of elements within the row.
        4. Horizontal line: Flips the entire matrix to reverse the order of rows.
        The user is prompted to choose an option, and the function performs the
        corresponding transposition. If an invalid choice is entered, an error message
        is displayed.

        Args:
            None

        Returns:
            None
    """
    print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    choice = input("Your choice: ")

    matrix = read_matrix()

    if choice == "1":
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif choice == "2":
        result = [[matrix[len(matrix) - 1 - j][len(matrix[0]) - 1 - i] for j in range(len(matrix))] for i in
                  range(len(matrix[0]))]
    elif choice == "3":
        result = [row[::-1] for row in matrix]
    elif choice == "4":
        result = matrix[::-1]
    else:
        print("Invalid choice.")
        return

    print("The result is:")
    for row in result:
        print(*row)


def calculate_determinant(matrix):
    """
        Calculates the determinant of a square matrix.
        This function recursively calculates the determinant of a square matrix using
        the cofactor expansion method. It works for matrices of any size greater
        than 1x1.

        Args:
            matrix: A list of lists representing a square matrix.

        Returns:
            float: The determinant of the input matrix.
    """
    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(n):
            submatrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
            determinant += (-1) ** j * matrix[0][j] * calculate_determinant(submatrix)
        return determinant


def determinant():
    """
        Calculates the determinant of a square matrix entered by the user.
        This function prompts the user to enter the size and elements of a matrix.
        It then checks if the matrix is square (equal number of rows and columns).
        If not, an error message is displayed. Otherwise, it calculates the determinant
        of the matrix using the `calculate_determinant` function and prints the result.

        Args:
            None

        Returns:
            None
    """
    matrix = read_matrix()
    if len(matrix) != len(matrix[0]):
        print("The matrix must be square.")
        return

    det = calculate_determinant(matrix)
    print("The result is:", det)


def inverse_matrix():
    """
        Calculates the inverse of a square matrix entered by the user.
        This function prompts the user to enter the size and elements of a matrix.
        It then checks if the matrix is square (equal number of rows and columns).
        If not, an error message is displayed. Otherwise, it calculates the determinant
        of the matrix. If the determinant is zero, the matrix is singular and does not
        have an inverse, so an error message is displayed.
        The function then prints the resulting inverse matrix.

        Args:
            None

        Returns:
            None
    """
    matrix = read_matrix()
    n = len(matrix)
    det = calculate_determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return

    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            submatrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            cofactor = (-1) ** (i + j) * calculate_determinant(submatrix)
            row.append(cofactor)
        cofactors.append(row)

    adjoint = [[cofactors[j][i] for j in range(n)] for i in range(n)]
    inverse = [[adjoint[i][j] / det for j in range(n)] for i in range(n)]

    print("The result is:")
    for row in inverse:
      print(" ".join(f"{elem:.2f}" for elem in row))


def main():
    """
    Provides a user interface for performing matrix operations.

       This function presents a menu-driven interface that allows the user to choose
       from various matrix operations.
       The program continues to loop and display the menu until the user chooses to exit.

       Args:
           None

       Returns:
           None
       """
    while True:
        print("\n1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_matrix_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            determinant()
        elif choice == "6":
            inverse_matrix()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
