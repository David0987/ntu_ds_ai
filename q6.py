def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    try:
        if isinstance(lst, list):
            while len(lst) > 0:
                val = lst.pop(0)
                if val < 0:
                    return val
            return 'No negatives'
        else:
            raise TypeError("The variable is not a list. Please try again.")
    except TypeError as e:
        print(e)






# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
