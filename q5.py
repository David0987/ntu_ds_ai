def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    try:
        if isinstance(num, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
            if num % divisor == 0:
                return True
            else:
                return False
        else:
            raise TypeError("The variable is not numeric. Please try again.")
    except TypeError as e:
        print(e)


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
