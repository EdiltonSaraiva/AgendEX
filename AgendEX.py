TarefasAgndex = []

def divisoria():
    print("-" * 49)


def MensagemDeSaida():
    print("\nSAIU DO PROGRAMA COM SUCESSO!\nOBRIGADO POR UTILIZAR.\n😁📴\n\n")


def ListarTarefa():
    print("\n", " " * 18, "📘 LISTAR TAREFAS 📚", " " * 18, "\n") 
    print("BEM-VINDO(A), À SESSÃO DE LISTAGEM DE TAREFAS👋!")
    print("AQUI VOCÊ VÊ TODAS AS SUAS TAREFAS CRIADAS PARA FICAR\nSEMPRE POR DENTRO DE TUDO O QUE PRECISA FAZER E SE \nMANTER ORGANIZADO(A).")
    divisoria()
    if len(TarefasAgndex) > 0:
        print(" " * 18, "SUAS TAREFAS: ", " " * 18)
        for indice_tarefa, tarefa in enumerate(TarefasAgndex, start = 1):
            print(f"{indice_tarefa} - {tarefa.upper()}")
        divisoria()
        print("O que deseja fazer agora?")
        print("1 - VOLTAR AO MENU INICIAL.")
        print("2 - MARCAR UMA TAREFA COMO CONCLUÍDA.")
        print("3 - EDITAR UMA TAREFA.")
        print("4 - ADICIONAR UMA NOVA TAREFA.")
        print("5 - SAIR DO AGENDEX 📒.")

        opc = input("\nDigite aqui o NÚMERO da ação que quer executar: ")

        if opc == "1":
            divisoria()
            print(f"AÇÃO {opc} SELECIONADA - VOLTAR AO MENU INICIAL")
            divisoria()
            MenuInicial()
        elif opc == "2":
            divisoria()
            print(f"AÇÃO {opc} SELECIONADA - MARCAR UMA TAREFA COMO CONCLUÍDA")
            divisoria()
            MarcarTerefaConcluida()
        elif opc == "3":
            divisoria()
            print(f"AÇÃO {opc} SELECIONADA - EDITAR UMA TAREFA")
            divisoria()
            EditarTarefa()
        elif opc == "4":
            divisoria()
            print(f"AÇÃO {opc} SELECIONADA - ADICIONAR UMA NOVA TAREFA")
            divisoria()
            NovaTarefa()
        elif opc == "5":
            divisoria()
            print(f"AÇÃO {opc} SELECIONADA - SAIR DO AGENDEX")
            divisoria()
            MensagemDeSaida()
        else: 
            divisoria()
            print("Ação inválida! Por favor, Tente novamente!")
            divisoria()
            ListarTarefa()
    else:
        divisoria()
        print("OPA...PARECE QUE VOCÊ NÃO ADICIONOU NENHUMA TAREFA AO SEU AGENDEX 😅")
        divisoria()
        print("Para adicionar uma nova tarefa volte ao Menu Inicial\ne selecione a opção '1 - ADICIONAR NOVA TAREFA'.\nFazendo isso, a partir do momento que uma tarefa\nfor criada, você poderá vê-la aqui.")
        print("\nDESEJA VOLTAR AO MENU INICIAL?")
        print("1 - SIM, VOLTAR.")
        print("2 - NÃO, QUERO FECHAR O AGENDEX.")

        opc_sem_tarefa = input("\nDigite aqui o NÚMERO da ação desejada: ")

        if opc_sem_tarefa == "1":
            divisoria()
            print(f" AÇÃO {opc_sem_tarefa} SELECIONADA - SIM, VOLTAR")
            MenuInicial()
        elif opc_sem_tarefa == "2":
            divisoria()
            print(f"AÇÃO SELECIONADA {opc_sem_tarefa} - NÃO, QUERO FECHAR O AGENDEX")
            divisoria()
            MensagemDeSaida()


ListarTarefa()



print("_" * 49)
print("\n                  A-G-E-N-D-E-X                  \n")
print("_" * 49)

def divisoria():
    print("-" * 49)


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


TarefasAgendex = []

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
