# Menú de opciones
historial = []

while True: 
    print("\nSelecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Pedir opción al usuario
    opcion = input("Elige una opción (1/2/3/4): ")

    # Pedir los números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Ejecutar la operación seleccionada
    if opcion == '1':
        resultado = num1 + num2
        print("Resultado de la suma:", resultado)
        historial.append(f"{num1} + {num2} = {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print("Resultado de la resta:", resultado)
        historial.append(f"{num1} - {num2} = {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print("Resultado de la multiplicación:", resultado)
        historial.append(f"{num1} * {num2} = {resultado}")
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado de la división:", resultado)
            historial.append(f"{num1} / {num2} = {resultado}")
        else:
            print("No se puede dividir entre cero")
            continue
    else:
        print("Opción no válida")
        continue

    # Preguntar si quiere continuar
    respuesta = input("\n¿Quieres hacer otra operación? (Si / No): ")
    if respuesta.lower() == 'no':
        print("\n--- Historial de Operaciones ---")
        for index, operacion in enumerate(historial, 1):
            print(f"{index}. {operacion}")
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
