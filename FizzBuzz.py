# Take input from the user. 
# If the input is divisible by 3 then print "Fizz",
# if the input it divisible by 5 then print "Buzz".
# If the input is divisible by 3 and 5 then print "Fizz Buzz".

number = int(input("Please enter a number:"))

def fizz_buzz(number):
    if (number % 3) == 0 and (number % 5) == 0:
        print("fizz buzz")
    elif (number % 3) == 0:
        print("fizz")
    elif (number % 5) ==0:
        print("buzz")
    else:
        print("This number is not divisable by 3 or 5")

fizz_buzz(number)


