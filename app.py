print("==========================================")
print("       PESQUISA DE ATENDIMENTO")
print("==========================================")

excelente = 0
ruim = 0

for i in range(1, 11):

    print(f"\n--- Entrevistado {i} ---")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    print("\nOpinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
        print(f"{nome}, sua resposta foi registrada como EXCELENTE.")

    elif opiniao == 2:
        print(f"{nome}, sua resposta foi registrada como BOM.")

    elif opiniao == 3:
        ruim += 1
        print(f"{nome}, sua resposta foi registrada como RUIM.")

    else:
        print("Opção inválida.")

print("\n==========================================")
print("          RESULTADO DA PESQUISA")
print("==========================================")

print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")