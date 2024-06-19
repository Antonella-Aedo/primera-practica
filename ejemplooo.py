def menu():
    print (".....menu.....")
    print("1) Verificar si un número es primo")
    print("2) Verificar si un número es par o impar")
    print("3) Calcular la suma de los números pares ingresados hasta el momento")
    print("4) alamcenar impar")
    print("5) Salir")

def num_primo(num):
    cont = 0
    x = 0
    while cont < num:
        cont += 1
        if num % cont == 0:
            x = x + 1
    if x == 2:
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")

def num_par(num):
    if num % 2 == 0:
        print(f"El número {num} es par.")
        return True
    else:
        print(f"El número {num} es impar.")
        return False

def almacenar_impar(num):
    if not num_par(num):
        with open("impares.txt", "a") as archivo:
            archivo.write(f"{num}\n")
       


        

