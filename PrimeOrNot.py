#Take input from the user and find out if that number is prime or not.

number = int(input("Please enter a number to determine whether it is a prime number:"))

for is_prime in range(2, number):
    if number % is_prime == 0:
        print("Not Prime!")
        break

else:
    print("Prime")


