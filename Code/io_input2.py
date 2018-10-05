forbiden = ('.', '?', '!', ':', ';', '-', '—', '(', ')', '[', ']', '...', '\'', '\"', '/', ',', ' ')

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Enter text:')

# Normalize the string
something = something.upper()
for item in forbiden:
    something = something.replace(item, '', -1)

if is_palindrome(something):
    print('Yes, it is a palindrome.')
else:
    print('No, it is not a palindrome.')