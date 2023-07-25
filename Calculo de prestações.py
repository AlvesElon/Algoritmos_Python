#entrada
valor_casa= float(input("Digite o valor da casa: "))
salario= float(input("digite seu salario: "))
anos= int(input("Em quantos anos pretende pagar: "))

#processamento
prestacao= valor_casa / (anos*12)

#finalização
if prestacao > 0.3*salario:
    input("financiamento negado")
elif prestacao <= 0.3*salario :
    input("financiamento aprovado")