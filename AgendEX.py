TarefasAgendex = []

def divisoria():
    print("-" * 49)

def marcar_tarefa_concluida():
    print("\nMARCAR TAREFA COMO CONCLUÍDA ✅")
    divisoria()

    if len(TarefasAgendex) == 0:
        divisoria()
        print("OPA...PARECE QUE VOCÊ NÃO ADICIONOU NENHUMA TAREFA AO SEU AGENDEX 😅")
        divisoria()
        print("Para marcar uma tarefa como concluída, primeiro adicione uma tarefa no menu inicial (opção 1).")
        return
    else:
        print("\nLISTA DE TAREFAS:")
        for i, tarefa in enumerate(TarefasAgendex, start=1):
            status = "✔ Concluída" if tarefa.get("concluida") else "⏳ Pendente"
            print(f"{i}. {tarefa['descricao']} — {status}")

        try:
            indice = int(input("\nDigite o número da tarefa que deseja marcar como concluída: ")) - 1

            if 0 <= indice < len(TarefasAgendex):
                if not TarefasAgendex[indice]["concluida"]:
                    TarefasAgendex[indice]["concluida"] = True
                    print("\nTarefa marcada como concluída com sucesso! ✔\n")
                else:
                    print("\nEsta tarefa já está marcada como concluída.\n")
            else:
                print("\nNúmero inválido! Nenhuma tarefa alterada.\n")

        except ValueError:
            print("\nEntrada inválida! Digite apenas números.\n")

        print("\nDESEJA VOLTAR AO MENU INICIAL?")
        print("1 - SIM, VOLTAR.")
        print("2 - NÃO, QUERO FECHAR O AGENDEX.")

        opc_sem_tarefa = input("\nDigite aqui o NÚMERO da ação desejada: ")

        if opc_sem_tarefa == "1":
            print(f"AÇÃO {opc_sem_tarefa} SELECIONADA - SIM, VOLTAR")
            MenuInicial()
        elif opc_sem_tarefa == "2":
            print(f"AÇÃO SELECIONADA {opc_sem_tarefa} - NÃO, QUERO FECHAR O AGENDEX")
            divisoria()
            print("\nSAIU DO PROGRAMA COM SUCESSO!\nOBRIGADO POR UTILIZAR.\n😁📴\n\n")
            exit()
        else:
            divisoria()
            print("Ação inexistente! Tente novamente!")
            divisoria()


print("_" * 49)
print("\n                  A-G-E-N-D-E-X                  \n")
print("_" * 49)
print("___________________MENU INCIAL___________________\n")
print("Bem-vindo(a) ao AgendEX! 📒  \nAqui você organiza suas tarefas com facilidade.\n")
print("-Selecione uma opção abaixo:\n")
print("1️⃣  - ADICIONAR NOVA TAREFA.")
print("2️⃣  - LISTAR TAREFAS EXISTENTES.")
print("3️⃣  - MARCAR TAREFA COMO CONCLUÍDA.")
print("4️⃣  - EDITAR TAREFA.")
print("5️⃣  - REMOVER TAREFA.")
print("6️⃣  - AJUDA E DÚVIDAS.")
print("7️⃣  - SAIR DO SISTEMA.\n")


opcao = (input("Por favor, digite o número da opção desejada: "))

if opcao == "1":
    print(f"\nOPÇÃO {opcao} SELECIONADA - ADICIONAR NOVA TAREFA  📝")
    divisoria()
    print()
elif opcao == "2":
    print(f"\nOPÇÃO {opcao} SELECIONADA - LISTAR TAREFAS EXISTENTES  🗃️")
    divisoria()
    print()
elif opcao == "3":
    print(f"OPÇÃO {opcao} SELECIONADA - MARCAR TAREFA COMO CONCLUÍDA  ✅")
    divisoria()
    print()
elif opcao == "4":
    print(f"\nOPÇÃO {opcao} SELECIONADA - EDITAR TAREFA  ✏️")
    divisoria()
    print()
elif opcao == "5":
    print(f"\nOPÇÃO {opcao} SELECIONADA - REMOVER TAREFA  🗑️")
    divisoria()
    print()
elif opcao == "6":
    print(f"\nOPÇÃO {opcao} SLECIONADA - AJUDA E DÚVIDAS ❓")
    divisoria()
    print()
elif opcao == "7":
    print(f"\nOPÇÃO {opcao} SELECIONADA - SAIR DO SISTEMA")
    divisoria()
    print("\nSAIU DO PROGRAMA COM SUCESSO!\nOBRIGADO POR UTILIZAR.\n😁📴\n\n")
else:
    divisoria()
    print("\nERRO! OPÇÃO DIGITADA NÃO EXISTE ❌\n\n")
