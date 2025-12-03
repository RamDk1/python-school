def is_palindrome(string):
    f = ''.join(c.lower() for c in string if c.isalnum())
    b = f[::-1]
    return f == b

phrase = str(input("Enter a phrase: "))
print(is_palindrome(phrase))