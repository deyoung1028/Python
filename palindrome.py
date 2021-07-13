# Create an app which detects if the input word is a palindrome or not.
# Hint - You can loop through a String. A String can be accessed like an array.



user_input = input("Please enter a word to determine if it is a palindrome:")

def is_palindrome(user_input):
    reversed_word = ""
    for index in range(len(user_input)-1, -1, -1):
        reversed_word = reversed_word + user_input[index]
    
    if user_input == reversed_word: 
        return True 
    else: 
        return False 

result = is_palindrome(user_input)
if result: 
    print("PALINDROME")
else: 
    print("NOT")

