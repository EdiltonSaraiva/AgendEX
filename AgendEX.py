TarefasAgendex = []

def divisoria():
    print("-" * 49)

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


    TarefasAgendex = []

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
