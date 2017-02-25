def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)
something = input("Enter text:")
strtxt = str(something)

newtext = strtxt.replace(",","")
print(newtext)
print(reverse(something))
print(is_palindrome(newtext))
if is_palindrome(newtext):
    print("yes,it is a palindrome")
else:
    print("no,it is not a palindrome")

