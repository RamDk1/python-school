def cal():

    num1 = float(input("Numero 1: "))
    operacion = input("(+,/,-,*):")
    num2 = float(input("Numero 2: "))

    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "-":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error division"
    else:
        return "None"
    
resultado = cal()
print(f"{resultado}")
