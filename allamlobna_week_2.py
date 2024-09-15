'''2. Uses conditionals (if-then-else) and exception handling.'''

try:
    value = int(input("Provide an even number:"))
except ValueError:
    print("The input provided is not a number.")
else:
    if value%2 == 0:
        print('The number is even.')
    else:
        print('The number is odd.')
