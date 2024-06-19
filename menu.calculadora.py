from calculadora import *

n1 = float(input("digite um valor"))
n2 = int(input("digite um valor"))
op = int(input("Digite 1 para soma\n"
               "Digite 2 para subtracao,\n"
               "digite 3 para multiplicacao\n"
               "digite 4 para divisao\n"
               "digite 5 para exponencial\n"
               "digite 6 para percentual\n"
               "digite 7 para fatorial"))

if(op == 1):
    resultado= soma(n1,n2)
    print(resultado)

elif(op == 2):
    resultado= subtracao(n1,n2)
    print(resultado)

elif(op == 3):
    resultado= multiplicacao(n1,n2)
    print(resultado)

elif(op == 4):
    resultado= divisao(n1,n2)
    print(resultado)

elif(op == 5):
    resultado= exponencial(n1,n2)
    print(resultado)

elif(op == 6):
    resultado= percentual(n1,n2)
    print(resultado)

elif(op == 7):
    resultado= fatorial(n2)
    print(resultado)