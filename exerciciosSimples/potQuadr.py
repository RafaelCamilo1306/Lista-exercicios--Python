def verifyAws(resposta):
    continua=["Sim","Yes", "Y", "S"]
    for answer in continua:
        if resposta.lower() in answer.lower(): #verifica independende se for maiusula a resposta do usuário com do sistema permitido 
            return True
    return False

repeat=True
while repeat:
    num1=int(input("\nDigite o 1° numero: "))
    num2=int(input("\nDigite o 2° numero: "))

    potencia= num1**num2

    print(f"\na exponenciação de {num1}^{num2}={potencia}")
    print(f"a raiz quadrada do numeros {num1} e {num2} são respectivamente {num1**(1/2)} e {num2**(1/2)}")
    resp= input("\nDeseja continuar?")

    if verifyAws(resp) :
        print("\nvamos de novo")
        repeat= True
    else:
        print("\nfim da execução")
        repeat=False