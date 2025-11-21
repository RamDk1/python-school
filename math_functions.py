# Illustrate calling a function and printing the result
# Ramses Rodriguez 11/3/2024

# Define functions
def addeight(n):
    """Returns the numerical value of n + 8, where n is an integer or float"""
    return n + 8

def multiplyby25(n):
    """Returns the numerical value of n * 25, where n is an integer or float"""
    return n * 25

def sum_odd_numbers(limit):
    """Returns the sum of all odd numbers from 1 to the specified limit"""
    total = 0
    for num in range(1, limit + 1, 2):  # Step by 2 to only include odd numbers
        total += num
    return total

def main():
    """This is where you define your variables and do input and output"""
    
    anum = int(input("Enter a number: "))
    print("Your number plus 8 is", addeight(anum))
    print("Your number multiplied by 25 is", multiplyby25(anum))
    
    limit = int(input("Enter the limit for summing odd numbers: "))
    print("The sum of all odd numbers from 1 to", limit, "is", sum_odd_numbers(limit))
    
# Call main function - should be last statement in your file
main()
