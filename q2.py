def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    
    try:
        if isinstance(lst, list):
            for idx, val in enumerate(lst):
                if val == find_val:
                    lst[idx] = replace_val
            return lst
        else:
            raise TypeError("The variable is not a list. Please try again.")
    except TypeError as e:
        print(e)


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"