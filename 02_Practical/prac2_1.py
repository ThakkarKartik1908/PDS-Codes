#2.1
def is_palindrome(text):
  if(text == text[::-1]):
    return True
  else :
    return False
#input
i = input("enter a text :")

if(is_palindrome(i)):
  print("text is palindrome")
else:
  print("text is not palindrome")