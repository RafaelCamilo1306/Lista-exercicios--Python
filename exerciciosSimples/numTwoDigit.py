while True:
    num= int(input("Escreva um numero: "))
    if (num<10) or (num>99):
        print(f"{num} o numero tem {len(str(num))} digitos.... \nesperava numeros com 2 digitos.....\n \n... fim da execução")
        break
