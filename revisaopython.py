# algaritimo -> sequencias de passos para executar uma tarefa

# estrutura possiveis no algaritimos
# 1 estrutural(sequncia de passos continuos)
# 2 condicional(DECISAO- vou executar uma script se acontcer x e outra se y)
# 3 repeticao(permite executar varias vezes o mesmo codigo)

# variaveis
# espacos de memoria que pode amazenar dados a execucao de um processos

# int,float,string e boolen
# int:(1(um so valor)) armazena valores  inteiros(10,14,31)
# float:(1.(ponto)(valor quebrado)) numeros decimais (12.1,23.4)
# string:cadeia de caracteristicas:nome de uma rua"roa bobos numero 45"sao valores literais ou seja nao 
# vou fazer calculos ex:Kaio,Luiz,Claudio.
# rua nome da rua, n0
# regars-> uma string deve estar entre "",'' "house's fer"
# boolean : e o poligrafo el aceita dois valores truem(verdadeiro) e false(falso)
#  VARIAVEL
# curso = "manufatura digital"
# a variavel "curso" recebe o valor "manufatura digital"

# print(type(curso))

#exibir -> comando print
# print("ola eu sou um print,estou executando seu py")

#para conversar com seu usuario eu sou o input
# altura = float(input("digite sua altura"))
# a variavel alturea recebe um valor quebrado de altura

# print(f"sua altura e {altura}")
# exibir para mim a "FORMATACAO" do texto com o valor de uma variavel

# nome = input("digite seu nome")
# sobrenome = input("digite seu sobrenome")
# print(nome + sobrenome)

# print("cadastro de uma pessoa")
# nome = input("digite seu nome")
# # idade = input("digite sua idade")
# endereço = input("digite seu endereço")
# cpf = input("digite seu cpf")
# distancia = input("digite a distancia percorrida no dia")
# anodeNacimento = int(input("digite o ano de nacimento"))
# idade = 2024 - anodeNacimento
# print(idade)


# estrutura de algaritimo CONDICIONAL
# executar alguma instrucao de acordo com os dados que eu tenho,por exemplo, so posso me alistar no exercito
# se for o IF ou else, eu tenho que saber quais as opcoes que eu tenho

# if(idade >= 18):
# se a idade for maior ou igual a 18 ENTAO exiba a mensagem
#     print("voce ja pode se alistar")
# else
# se a idade nao for maior ou igual a 18 ENTAO(:)exiba a mensagem
    # print("voce e menor de idade")

# nota = float(input("informe a nota 1"))

# if (nota>5):
#     print("voce esta aprovado")
# elif(nota == 5):
#     print("chama os pais,pq vc esta no conselho")
# else:
#     print("voce esta reprovado")


# se o salario for maior doq 1500 adicione 500
# se o salario for maior do que 2000 some 400
# se o salario for maior do que 3000 some 300

salario = float(input("informe seu salario"))
if (salario <=1500):
    print(f"seu salrio e {salario + 500}")

elif(salario <= 2000):
    print(f"seu salaro e {salrio + 400}")
elif (salrio >= 3000):
    print(f"seu salrio e {salario + 300}")

else:
    print("falta dinheiro")


