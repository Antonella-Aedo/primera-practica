from ejemplooo import num_primo, num_par, menu, almacenar_impar

suma_pares = 0
while True: 
        menu()
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError: 
            print("Error: Por favor, ingrese una opción válida (número entero).")
        if opcion == 1:
            try:
                num = int(input("Ingrese un número entero positivo: "))
                num_primo(num) 
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido.")          
        elif opcion == 2:
            try:
                num = int(input("Ingrese un número: "))
                if num_par(num):
                    suma_pares=suma_pares+num
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido.")
        elif opcion == 3:
            print(f"La suma de los números pares ingresados hasta el momento es: {suma_pares}") 
        elif opcion ==4:
            almacenar_impar(num)
            print(f"El número {num} ha sido almacenado en impares.txt.")
        elif opcion == 5:
            print("Saliendo del programa.")
            break 
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 4.")

print( "hola ")

