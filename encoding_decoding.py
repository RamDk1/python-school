def enc(str):
    L = []
    prev = str[0]
    count = 0
    for char in str:
        if prev != char:
            L.append((prev, count))
            count = 0
        prev = char
        count += 1
    L.append((prev, count))
    return L

def dec(L):
    str = ""
    for char in L:
        str = str + char[0] * char[1] 
    return str

print(enc("aaabbbccdaa"))
print(dec([('a', 3), ('b', 3), ('c', 2), ('d', 1), ('a', 2)]))
