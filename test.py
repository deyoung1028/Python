number = int(input("Give me a number: "))

for is_prime in range(2, number):
    if number % is_prime == 0:
        print("Not Prime!")
        break
else:
    print("Prime Number!")