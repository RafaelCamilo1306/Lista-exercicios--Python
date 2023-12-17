#programa para aprovar/reprovar aluno com base nas suas mêdias 

print("="*25)
print("Bem vindo a calculadora de aprovação")
print("="*25)

print("insira as notas do aluno")

notas=input("digite todas as notas separadamente:[ex: 6 7 8]\n")

listaNotas="".join(notas).split()

somaNotas=0

for nota in listaNotas:
    somaNotas+=int(nota)

media=somaNotas/len(listaNotas)

if media>=7:
    print(f"Aluno aprovado com uma media de {media}")
else:
    print(f"Aluno reprovado com uma media de {media} o minimo era 7")

