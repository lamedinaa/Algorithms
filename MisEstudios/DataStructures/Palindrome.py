##Palindrome problem
##Palindrome is a string that reads the same forward and backward  Ex: radar or madam
from ReverseArray import reverse_string

def palindrome_python(s):
    if s == s[::-1]:
        return True
    return False

def is_palindrome(s):
    if s == reverse_string(s):
        return True
    return False


if __name__ == '__main__':
    print(palindrome_python("madam"))
    print(is_palindrome("madam"))