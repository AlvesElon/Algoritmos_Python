#entrada
nome=input("informe o nome do aluno: ")
n1=float(input("informe a primeira nota: "))
n2=float(input("informe a segunda nota: "))
n3=float(input("informe a terceira nota: "))

#processamento
mediafinal=((n1*2) + (n2*3) + (n3*5)) /10

#saida
print("O aluno", nome, "recebeu nota", mediafinal)