# Write an app which ask user for an input and then displays a message indicating whether the number is even or odd.

number = int(input('Enter a number:'))

def even_odd(number):
    if number % 2 == 0:
        print( "Your number is even.")
    else:
        print("Your number is odd.")

even_odd(number)
