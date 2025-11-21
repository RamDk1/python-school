hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hx(str):
    str = str.upper()
    for char in str:
        if char not in hexNumbers:
            return None
        
    v = 0
    ex = len(str) - 1

    for char in str:
        v = v + hexNumbers[char] * (16**ex)
        ex = ex - 1
    
    return v

print(hx("1A3F"))  # Example usage
