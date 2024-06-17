def controledevelocidade():
    velocidade = 50
    contator = 0
    print("Chamou")
    while contator < 10 and velocidade >= 0 and velocidade <= 100:
        print(f"velocidade atual= {velocidade} km")
        opcao = input("deseja aumentar (A) ou diminuir (D) a velocidade?").strip().upper()
        if opcao == "A":
            velocidade += 10
        elif opcao == "D":
            velocidade -= 10
        else:
            print("escolha invalida,tente novamente.")
            continue

        contator += 1

        if velocidade <= 0 or velocidade >= 100:
            break
        print(f"operacao finalizada,velocidade final: {velocidade} km")

controledevelocidade()

