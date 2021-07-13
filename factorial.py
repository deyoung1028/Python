# Write an app which asks users for the input and then prints the factorial for that number.

number = int(input("Please enter a number:"))

factorial = 1

for current_number in range(1, number + 1):
  factorial *= current_number
print("The factorial of", number, "is", factorial)
