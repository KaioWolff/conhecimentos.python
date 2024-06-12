def controlevelocidade():
    velocidade = 50
    contator = 0

while contatortentativas < 10 and 0 <= velocidade <= 100:
    print(f"velocidade atual: {velocidade} km")
    input=("deseja aumentar (A) ou diminuir (D) a velocidade?")
    if opcao == "A":
        velocidade += 10
    elif opcao == "D":
        velocidade -= 10

    else:
        print("escolha invalida,tente novamente.")

    contator += 1

    if velocidade <= 0 or velocidade >= 100:
        break
     print(f "operacao finalizada,velocidade final: {velocidade} km")

