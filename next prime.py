# Python3 implementation of the approach
import math


# Function that returns True if n
# is prime else returns False
def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False

    return True


# Function to return the smallest
# prime number greater than N
def nextPrime(num):
    # Base case
    if (num <= 1):
        return 2

    prime = num
    found = False

    # Loop continuously until isPrime returns
    # True for a number greater than n
    while (not found):
        prime = prime + 1

        if (isPrime(prime) == True):
            found = True

    return prime


# Driver code
num = int(input('input the number you want to start its prime sequence: '))
while True:
    response = input('do you wanna print next prime? (y/n): ')
    boolean = False

    if response == 'y':
        print(nextPrime(num))
        num = nextPrime(num)
    elif response == 'n':
        break
