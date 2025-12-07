TarefasAgendex = []

def divisoria():
    print("-" * 49)


def MensagemSemTarefa():
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
                MensagemSemTarefa()


def EditarTarefa():
    def EditandoTarefa():
        if len(TarefasAgendex) > 0:
            divisoria()
            print("POR FAVOR, PARA PROSSEGUIR, SELECIONE A TAREFA QUE VOCÊ DESEJA EDITAR: ")
            divisoria()
            for indice_tarefa, tarefa in enumerate(TarefasAgendex, start = 1):
                print(f"{indice_tarefa} - {tarefa.upper()}")

            indice_usuario = 0

            try: 
                indice_usuario = int(input("\nDigite o NÚMERO da tarefa que deseja editar: "))
                divisoria()
                print(f"VOCÊ ESTÁ EDITANDO A TAREFA DE NÚMERO {indice_usuario} - {TarefasAgendex[indice_usuario - 1]}")
            except ValueError:
                divisoria()
                print("Por favor, digite apenas números! Tente novamente!")
                divisoria()
                EditarTarefa()
            except IndexError:
                divisoria()
                print("A tarefa que você tentou acessar, não existe! Tente novamente!")
                divisoria()
                EditarTarefa()
            else:
                indice_tarefa = indice_usuario - 1
                divisoria()
                TarefasAgendex[indice_tarefa] = input("Digite aqui a nova descrição da tarefa: ")
                divisoria()
                print("TAREFA ATUALIZADA COM SUCESSO ✅!")
                print("PARA VER SUAS TAREFAS, VOLTE AO MENU\nINICIAL E SELECIONE A OPÇÃO\n'2 - LISTAR TAREFAS EXISTENTES'")
                divisoria()


                def ContinuarEditando():
                    print("\nVocê deseja editar alguma tarefa, ou voltar ao menu inicial?")
                    print("1 - SIM, EDITAR.")
                    print("2 - NÃO, VOLTAR AO MENU INICIAL.")

                    opc = input("Digite aqui o NÚMERO da ação desejada: ")

                    if opc == "1":
                        divisoria()
                        print(f"AÇÃO {opc} SELECIONADA - SIM, EDITAR")
                        divisoria()
                        print("\n", " " * 18, "CONTINUAR EDITANDO", " " * 18, "\n")
                        EditandoTarefa()
                    elif opc == "2":
                        divisoria()
                        print(f"AÇÃO {opc} SELECIONADA - NÃO, VOLTAR AO MENU INICIAL")
                        divisoria()
                        MenuInicial()
                    else:
                        divisoria()
                        print("A ação digitada não existe! Tente novamente!")
                        divisoria()
                        ContinuarEditando()


            ContinuarEditando()

        else:
            MensagemSemTarefa()


    print("\n", " " * 18, "✍️  EDITAR TAREFAS 🧩", " " * 18, "\n")
    print("BEM-VINDO(A), À SESSÃO DE EDIÇÃO DE TAREFAS DO AGENDEX 📒!")
    print("SE VOCÊ PRECISA FAZER ALTERAÇÕES EM UMA TAREFA\nQUE VOCÊ CRIOU, ESTÁ NO LUGAR CERTO! EDITE AS\nTAREFAS QUE VOCÊ PRECISA.")

    EditandoTarefa()












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


