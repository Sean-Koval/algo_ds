x = 32


def reverse_int(x):

    string = str(x)

    if string[0] == '-':
        return int('-' + string[:0:-1])


### HOW TO REVERSE A STRING WITHOUT [::-1] or .reverse() ###
## checks if a string is a palindrome
def reverse_string(x):

    m = ''

    # this reverses the string
    for i in x:
        m = i + m

    if m == x:
        return True
    else:
        return False



