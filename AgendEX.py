TarefasAgendex = []

def divisoria():
    print("-" * 49)


def MensagemSemTerefa():
    divisoria()
    print("OPA...PARECE QUE VOCÊ NÃO ADICIONOU NENHUMA TAREFA AO SEU AGENDEX 😅")
    divisoria()
    print("Para adicionar uma nova tarefa volte ao Menu Inicial\ne selecione a opção '1 - ADICIONAR NOVA TAREFA'.\nFazendo isso, a partir do momento que uma tarefa\nfor criada, você poderá editá-la.")
    print("\nDESEJA VOLTAR AO MENU INICIAL?")
    print("1 - SIM, VOLTAR.")
    print("2 - NÃO, QUERO FECHAR O AGENDEX.")

    opc_sem_tarefa = input("\nDigite aqui o NÚMERO da ação desejada: ")

    if opc_sem_tarefa == "1":
        print(f" AÇÃO {opc_sem_tarefa} SELECIONADA - SIM, VOLTAR")
        MenuInicial()
    elif opc_sem_tarefa == "2":
        print(f"AÇÃO SELECIONADA {opc_sem_tarefa} - NÃO, QUERO FECHAR O AGENDEX")
        divisoria()
        print("\nSAIU DO PROGRAMA COM SUCESSO!\nOBRIGADO POR UTILIZAR.\n😁📴\n\n")
    else:
        divisoria()
        print("Ação inexistente! Tente novamente!")
        divisoria()
        MensagemSemTerefa()


def RemoverTarefa():
    print("\n", " " * 18, "🗑️ REMOVER TAREFA 📄", " " * 18, "\n")
    print("BEM-VINDO(A) A SESSÃO DE REMOÇÃO DE TAREFAS DO AGENDEX 👋!")
    print("SE VOCÊ DESJA EXCLUIR UMA TAREFA DO SEU\nAGENDEX 📒, É AQUI QUE VOCÊ FAZ ISSO!")
    if len(TarefasAgendex) > 0:
        divisoria()
        print(" " * 18, "SUAS TAREFAS:", " " * 18)
        for indice_tarefa, tarefa in enumerate(TarefasAgendex, start = 1):
                print(f"{indice_tarefa} - {tarefa.upper()}")
        divisoria()

        indice_usuario = 0

        try:
            indice_usuario = int(input("Digite aqui o NÚMERO da tarefa que deseja remover: "))
            divisoria()
            print(f"VOCÊ ESTÁ EXLCUINDO A TAREFA DE NÚMERO {indice_usuario} - '{TarefasAgendex[indice_usuario - 1]}'")
        except ValueError:
            divisoria()
            print("Por favor, digite apenas números! Tente novamente!")
            divisoria()
            RemoverTarefa()
        except IndexError:
            divisoria()
            print("A tarefa que você tentou excluir, nã existe! Tente novamente!")
            divisoria()
            RemoverTarefa()
        else:
            indice_tarefa = indice_usuario - 1
            divisoria()
            TarefasAgendex.pop(indice_tarefa)
            print("TAREFA EXCLUÍDA COM SUCESSO ✅!")
            print("PARA VER SUAS TAREFAS, VOLTE AO MENU\nINICIAL E SELECIONE A OPÇÃO\n'2 - LISTAR TAREFAS EXISTENTES'")
            divisoria()

            def ContinuarRemovendo():
                print("Você desejar voltar ao menu inicial ou continuar exlcuindo tarefas?")
                print("1 - VOLTAR AO MENU INICIAL.")
                print("2 - CONTINUAR EXLCUINDO.")

                opc = input ("Digite aqui o NÚMERO da ação que deseja realizar: ")

                if opc == "1":
                    divisoria()
                    print(f"AÇÃO {opc} SELECIONADA - VOLTAR AO MENU INICIAL")
                    MenuInicial()
                elif opc == "2":
                    divisoria()
                    print(f"AÇÃO {opc} SELECIONADA - CONTINUAR EXCLUINDO")
                    divisoria()
                    RemoverTarefa()
                else:
                    divisoria()
                    print("A ação digitada não existe! Por favor, tente novamente!")
                    divisoria()
                    ContinuarRemovendo()


        ContinuarRemovendo()

    else:
        MensagemSemTerefa()


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
    RemoverTarefa()
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

