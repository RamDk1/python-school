OUNCES_PER_QUART = 32
QUARTS_PER_BARREL = 168 
numquarts = int(input("Enter the number of quarts: "))

numbarrels = numquarts // QUARTS_PER_BARREL
remquarts = numquarts % QUARTS_PER_BARREL

numounces = numquarts * OUNCES_PER_QUART

print(f"{numquarts} quarts is {numbarrels} and {remquarts}")
print(f"That is {numounces} ounces")