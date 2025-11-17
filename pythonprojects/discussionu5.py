#Ramses Rodriguez 
# Reply post discussion unit 5

# Get input from the user
weekend = input("What is your favorite thing to do on the weekends?: ")

def count_spaces(aString):
   
    # Use the count method to find the number of spaces in the string
    space_count = aString.count(' ')
    
    # Return the number of spaces found
    return space_count

# Call the function with the user's input and print the result
result = count_spaces(weekend)
print("The number of spaces in the string is:", result)

long = "I am testing this program with a slightly longer sentence and using a different parameter to complete the task I was assigned."
espacio = count_spaces(long)
print(f"The number of spaces in \"{long}\" is: {espacio}")