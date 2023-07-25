#entrada
nome= input("informe seu nome: ")
ano_atual= int(input("informe o ano atual: "))
ano_nascimento= int(input("informe seu ano de nascimento: "))
    
#processamento
idade = ano_atual - ano_nascimento

#finalização
print("caro", nome,"sua idade é", idade)
if idade <= 3:
    print("você é um bebê")
elif idade <= 12:
    print("você é juvenil!!")
elif idade <= 19:
    print("você é adolescente")
elif idade <= 59:
    print("você é adulto")
elif idade <= 100:
    print("você é velho")
elif idade <= 120:
    print("Cuidado ao levantar os braços... Deus puxa")
else:
    print("Você é uma antiguidade")