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


print("_" * 49)
print("\n                  A-G-E-N-D-E-X                  \n")
print("_" * 49)
TarefasAgendex = []

def divisoria():
    print(" " * 49)


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
    ListarTarefa()
elif opcao == "3":
    print(f"OPÇÃO {opcao} SELECIONADA - MARCAR TAREFA COMO CONCLUÍDA  ✅")
    divisoria()
    print()
elif opcao == "4":
    print(f"\nOPÇÃO {opcao} SELECIONADA - EDITAR TAREFA  ✏️")
    divisoria()
    EditarTarefa()
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


def MarcarConcluida():
    print("\n", " " * 9, "📗 MARCAR TAREFA CONCLUIDA 📝", " " * 9, "\n")
    print("BEM-VINDO(A) A SESSÃO DE MARCAR TAREFAS CONCLUÍDAS DO AGENDEX 👋!")
    print("SE VOCÊ CONCLUIU AQUELA DEMANDA E DESEJA\nSINALIZAR, É AQUI QUE VOCÊ FAZ ISSO!")
    if len(TarefasAgendex) > 0:
        divisoria()
        print(" " * 18, "SUAS TAREFAS:", " " * 18)
        for indice_tarefa, tarefa in enumerate(TarefasAgendex, start = 1):
                print(f"{indice_tarefa} - {tarefa.upper()}")
        divisoria()

        indice_usuario = 0

        try:
            indice_usuario = int(input("Digite aqui o NÚMERO da tarefa que você já concluiu: "))
            divisoria()
            print(f"VOCÊ CONCLUIU A TAREFA DE NÚMERO {indice_usuario} - '{TarefasAgendex[indice_usuario - 1]}'")
        except ValueError:
            divisoria()
            print("Por favor, digite apenas números! Tente novamente!")
            divisoria()
            MarcarConcluida()
        except IndexError:
            divisoria()
            print("A tarefa que você tentou concluir, não existe! Tente novamente!")
            divisoria()
            MarcarConcluida()
        else:
            if " - CONCLUÍDA ✔️" in TarefasAgendex[indice_usuario - 1]:
                divisoria()
                print("A tarefa selecionada já foi concluída! Tente outra!")
                divisoria()
                MarcarConcluida()
            else:
                indice_tarefa = indice_usuario - 1

                TarefasAgendex[indice_tarefa] = TarefasAgendex[indice_tarefa] + " - CONCLUÍDA ✔️"
                divisoria()
                print("\nTAREFA CONCLUÍDA COM SUCESSO ✅!\n")
                for indice_tarefa, tarefa in enumerate(TarefasAgendex, start = 1):
                    print(f"{indice_tarefa} - {tarefa.upper()}")

def MenuInicial():
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
        NovaTarefa()
    elif opcao == "2":
        print(f"\nOPÇÃO {opcao} SELECIONADA - LISTAR TAREFAS EXISTENTES  🗃️")
        divisoria()
        ListarTarefas()
    elif opcao == "3":
        print(f"OPÇÃO {opcao} SELECIONADA - MARCAR TAREFA COMO CONCLUÍDA  ✅")
        divisoria()
        MarcarConcluida()
    elif opcao == "4":
        print(f"\nOPÇÃO {opcao} SELECIONADA - EDITAR TAREFA  ✏️")
        divisoria()
        EditarTarefa()
    elif opcao == "5":
        print(f"\nOPÇÃO {opcao} SELECIONADA - REMOVER TAREFA  🗑️")
        divisoria()
        RemoverTarefa()
    elif opcao == "6":
        print(f"\nOPÇÃO {opcao} SLECIONADA - AJUDA E DÚVIDAS ❓")
        divisoria()
        AjudaDuvidas()
    elif opcao == "7":
        print(f"\nOPÇÃO {opcao} SELECIONADA - SAIR DO SISTEMA")
        divisoria()
        print("\nSAIU DO PROGRAMA COM SUCESSO!\nOBRIGADO POR UTILIZAR.\n😁📴\n\n")
    else:
        divisoria()
        print("\nERRO! OPÇÃO DIGITADA NÃO EXISTE ❌\n\n")


def NovaTarefa():
    def ContinuarAdicionando():
        print("\nDeseja adicionar uma nova tarefa ou voltar ao menu inicial?")
        print("1 - ADICIONAR.")
        print("2 - VOLTAR AO MENU INICIAL.")

        continuar_adicionando = input("Digite aqui o NÚMERO da ação que deseja: ")

        if continuar_adicionando == "1":
            divisoria()
            print(f"\nAÇÃO {continuar_adicionando} SELECIONADA - ADICIONAR")
            divisoria()
            TarefasAgendex.append(input("Descreva sua nova tarefa: "))
            divisoria()
            print("SUA TAREFA FOI ADICIONADA COM SUCESSO✅!")
            ContinuarAdicionando()
        elif continuar_adicionando == "2":
            divisoria()
            print(f"\nAÇÃO {continuar_adicionando} SELECIONADA - VOLTAR AO MENU INICIAL")
            divisoria()
            MenuInicial()  
        else:
            divisoria()
            print("Opção digitada não existe! Tente Novamente!")
            divisoria()
            ContinuarAdicionando()


    print("\n"," " * 18 ,"📝 ADICIONAR NOVA TAREFA 🆕", 18 * " ", "\n")
    print("BEM-VINDO(A), A SESSÃO DE ADICIONAR TAREFAS DO AGENDEX 👋!")
    print("É AQUI QUE VOCÊ FAZ A MAGIA ACONTECER! ADICIONE UMA\nTAREFA A SUA LISTA PARA SE MANTER ORGANIZADO(A).")
    divisoria()
    print("POR FAVOR, PARA PROSSEGUIR, CONFIRME SUA AÇÃO:")
    print("1 - ADICIONAR NOVA TAREFA AO AGENDEX📒.")
    print("2 - VOLTAR AO MENU INICIAL.")

    opc = input("\nDigite aqui o NÚMERO da ação desejada: ")

    if opc == "1":
        print(f"\nAÇÃO {opc} SELECIONADA - ADICIONAR NOVA TAREFA AO AGENDEX")
        divisoria()
        TarefasAgendex.append(input("Descreva sua nova tarefa: "))
        divisoria()
        print("SUA TAREFA FOI ADICIONADA COM SUCESSO✅!")
        divisoria()
        print("PARA VER SUAS TAREFAS, VOLTE AO MENU\nINICIAL E SELECIONE A OPÇÃO\n'2 - LISTAR TAREFAS EXISTENTES'")
        divisoria()
        ContinuarAdicionando()
    elif opc == "2":
        print(f"\nAÇÃO {opc} SLECIONADA - VOLTAR AO MENU INICIAL")
        divisoria()
        MenuInicial()
    else: 
        divisoria()
        print("Opção digitada não existe! Tente Novamente!")
        

print("Bem-vindo(a) ao AgendEX! 📒  \nAqui você organiza suas tarefas com facilidade.\n")
print("\nCONFIRME PARA ENTRAR NO AGENDEX 📒")
print("1 - CONFIRMAR")
print("2 - SAIR")

while True:
    opcao_inicio = input("Digite o NÚMERO da ação que deseja executar: ")

    if opcao_inicio == "1":
        divisoria()
        print(f"AÇÃO {opcao_inicio} SELECIONADA - CONFIRMAR")
        divisoria()
        MenuInicial()
    elif opcao_inicio == "2":
        divisoria()
        print(f"AÇÃO {opcao_inicio} SELECIONADA - SAIR")
        divisoria()
        break
    else:
        divisoria()
        print("A ação digitada não existe! Tente novamente!")
        divisoria()
