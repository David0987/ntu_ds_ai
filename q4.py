def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    try:
        if isinstance(s, str):
            reversed_lst = []    
            for i in range(len(s)):
                reversed_lst.append(s[i])
            reversed_lst.reverse()
            s = ''.join(reversed_lst)
            return s
        else:
            raise TypeError("The variable is not a string. Please try again.")
    except TypeError as e:
        print(e)


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
