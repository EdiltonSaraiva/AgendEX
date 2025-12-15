TarefasAgendex = []

def divisoria():
    print("-" * 49)


def MensagemDeSaida():
    print("\nSAIU DO PROGRAMA COM SUCESSO!\nOBRIGADO POR UTILIZAR.\n😁📴\n\n")
    exit()


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


    print("\n"," " * 9,"📝 ADICIONAR NOVA TAREFA 🆕", 9 * " ", "\n")
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
        NovaTarefa()

def MarcarConcluida():
    def ConcluirMais():
                print("\nVocê ainda deseja concluir alguma tarefa?")
                print("1 - SIM, CONCLUIR MAIS.")
                print("2 - NÃO, VOLTAR AO MENU INICIAL.")

                opc = input("Digite o NÚMERO da ação que deseja realizar: ")

                if opc == "1":
                    divisoria()
                    print(f"AÇÃO {opc} SELECIONADA - CONCLUIR MAIS")
                    MarcarConcluida()
                elif opc == "2":
                    divisoria()
                    print(f"AÇÃO {opc} SELECIONADA - VOLTAR AO MENU INICIAL")
                    MenuInicial()
                else:
                    divisoria()
                    print("A ação digitada não existe! Por favor, tente novamente!")
                    divisoria()
                    ConcluirMais()
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
                ConcluirMais()
            else:
                indice_tarefa = indice_usuario - 1

                TarefasAgendex[indice_tarefa] = TarefasAgendex[indice_tarefa] + " - CONCLUÍDA ✔️"
                divisoria()
                print("\nTAREFA CONCLUÍDA COM SUCESSO ✅!\n")
                for indice_tarefa, tarefa in enumerate(TarefasAgendex, start = 1):
                    print(f"{indice_tarefa} - {tarefa.upper()}")

        ConcluirMais()

    else:
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


def RemoverTarefa():
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
                    ContinuarRemovendo()
                else:
                    divisoria()
                    print("A ação digitada não existe! Por favor, tente novamente!")
                    divisoria()
                    ContinuarRemovendo()
    print("\n", " " * 18, "🗑️ REMOVER TAREFA 📄", " " * 18, "\n")
    print("BEM-VINDO(A) A SESSÃO DE REMOÇÃO DE TAREFAS DO AGENDEX 👋!")
    print("SE VOCÊ DESEJA EXCLUIR UMA TAREFA DO SEU\nAGENDEX 📒, É AQUI QUE VOCÊ FAZ ISSO!")
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
            print("Tem certeza que deseja remover a tarefa?")
            print("1 - CONFIRMAR REMOÇÃO.")
            print("2 - VOLTAR AO MENU INICIAL.")

            confirmar_exclusao = input("Digite o NÚMERO da ação desejada: ")

            if confirmar_exclusao == "1":
                TarefasAgendex.pop(indice_tarefa)
                divisoria()
                print(f"AÇÃO {confirmar_exclusao} SELECIONADA - CONFIRMAR REMOÇÃO")
                divisoria()
                print("TAREFA EXCLUÍDA COM SUCESSO ✅!")
                divisoria()
                print("PARA VER SUAS TAREFAS, VOLTE AO MENU\nINICIAL E SELECIONE A OPÇÃO\n'2 - LISTAR TAREFAS EXISTENTES'")
                divisoria()
                RemoverTarefa()
            elif confirmar_exclusao == "2":
                divisoria()
                print(f"AÇÃO {confirmar_exclusao} - VOLTAR AO MENU INICIAL")
                divisoria()
                MenuInicial()
            else:
                divisoria()
                print("Ação digitada não existe! Tente novamente!")
                divisoria()
                RemoverTarefa()
    else:
        MensagemSemTarefa()

def AjudaDuvidas():
    def SairVoltar():
        divisoria()
        print('Deseja FECHAR O PROGRAMA, VOLTAR AO MENU INCIAL ou PRECISA DE MAIS AJUDA?')
        print('1 - VOLTAR AO MENU INICIAL.')
        print('2 - PRECISO DE MAIS AJUDA.')
        print('3 - FECHAR O PROGRAMA AGORA.')
        divisoria()

        opc = input("Digite aqui o NÚMERO da opção desejada: ")

        if opc == "1":
            divisoria()
            print(f"OPCAO {opc} SELECIONADA - VOLTAR AO MENU INICIAL")
            divisoria()
            MenuInicial()
        elif opc == "2":
            divisoria()
            print(f"OPÇÃO {opc} - PRECISO DE MAIS AJUDA")
            divisoria()
            AjudaDuvidas()
        elif opc == "3":
            divisoria()
            MensagemDeSaida()
        else: 
            divisoria()
            ("A opção digitada não existe! Por favor, tente novamente.")
            divisoria()
    print("\n", " " * 9, "❓AJUDA E DÚVIDAS🤔", 9 * " ", "\n")
    print("BEM-VINDO(A), A SESSÃO DE AJUDA E DÚVIDAS DO AGENDEX 👋!")
    print("SE VOCÊ FICOU CONFUSO COM ALGUMA DAS FUNCIONALIDADES DO\nPROGRAMA É AQUI QUE VOCÊ OBTÉM AS RESPOSTAS QUE PROCURA.")
    divisoria()
    print("POR FAVOR, PARA PROSSEGUIR, SELECIONE UMA DÚVIDA\nNAS OPÇÕES DIPONÍVEIS ABAIXO:")
    print("1 - Como utilizar o programa?")
    print("2 - O que é o AgendEX?")
    print("3 - Onde posso ver minhas tarefas?")
    print("4 - É possível excluir uma tarefa?")
    print("5 - Há um limite de tarefas que eu posso criar?")
    print("6 - O que fazer depois de concluir uma tarefa?")
    print("0 - Voltar ao menu inicial.")
    divisoria()

    opc = input("Digite aqui o NÚMERO da sua dúvida: ")

    if opc == "1": 
        print(f"\nNÚMERO {opc} DIGITADO.\nSUA DÚVIDA É -> 'Como utilizar o programa?'\n")
        divisoria()
        print("--SOLUÇÃO--")
        print("Para utilizar o AgendEX📒, você deve:")
        print("-Antes de mais nada, executar o programa no terminal, editor de texto ou IDE, no seu computador;")
        print("-Seguir os comandos ao final de cada menu;")
        print("-Esteja ciente que no Menu Inicial e demais menus de opção, só são aceitos números, conforme indicado no comando. Ex: 'Digite o número da opção desejada';")
        print("-Ao selecionar a opção '7 - SAIR DO SISTEMA',  no Menu Inicial, o AgendEX é fechado imediatamente, sendo necessário reexecutá-lo para usar novamente.")
        print('\nEsperamos ter atentidido as suas dúvidas!\n')
        SairVoltar()
    elif opc == "2":
        print(f"\nNÚMERO {opc} DIGITADO.\nSUA DÚVIDA É -> 'O que é o AgendEX?'\n")
        divisoria()
        print("--SOLUÇÃO--")
        print("*O AgendEX📒 é um SISTEMA DE ORGANIZAÇÃO DE TAREFAS, nele você pode:")
        print("*Criar uma nova tarefa;")
        print("*Ver quais tarefas você já criou;")
        print("*Sinalizar uma tarefa como concluída;")
        print("*Exlcuir tarefas criadas;")
        print("*Editar tarefas criadas;")
        print("*E também pode vir aqui, na sessão de dúvidas e ajuda, ficar informado sobre o AgendEX.")
        print('\nEsperamos ter atentidido as suas dúvidas!\n')
        SairVoltar()
    elif opc == "3":
        print(f"\nNÚMERO {opc} DIGITADO.\nSUA DÚVIDA É -> 'Onde ver minhas tarefas?'\n")
        divisoria()
        print("--SOLUÇÃO--")
        print("Você pode sim ver suas tarefas criadas!")
        print("-No Menu Inicial, digite a opção '2 - LISTAR TAREFAS EXISTENTES';")
        print("-Ao selecionar essa opção, serão listadas todas as suas tarefas criadas;")
        print("-Caso você não tenha criado nenhuma tarefa, uma mensagem aparecerá na tela, notificando.")
        print('\nEsperamos ter atentidido as suas dúvidas!\n')
        SairVoltar()
    elif opc == "4":
        print(f"\nNÚMERO {opc} DIGITADO.\nSUA DÚVIDA É -> 'É possível exlcuir uma tarefa?'\n")
        divisoria()
        print("--SOLUÇÃO--")
        print("Sim! Você pode excluir tarefas, para isso, siga os seguintes passos:") 
        print("-No Menu Inicial, digite a opção '5 - REMOVER TAREFA';")
        print("-Após selecionada a opção, caso haja tarefas criadas, uma mensagem de selecionar tarefa será apresentada;")
        print("-Em seguida, você deve confirmar a exlcusão no menu, com a opção '1 - CONFIRMAR REMOÇÃO';")
        print("-Caso você não tenha nenhuma tarefa para ser exlcuída, uma mensagem notificando será exibida.")
        print('Esperamos ter atendido suas dúvidas!\n')
        SairVoltar()
    elif opc == "5":
        print(f"\nNÚMERO {opc} DIGITADO.\nSUA DÚVIDA É -> 'Há um limite de tarefas que eu posso criar?'\n")
        divisoria()
        print("--SOLUÇÃO--")
        print("Não! No AgendEX o céu é o limite!")
        print("Mas fica a dica: Não crie mais tarefas do que você pode ou consegue fazer!")
        print("Porém, opa...criou tarefas demais? Sem Problemas! Você pode excluir aquelas que achar coveniente.")
        print('Esperamos ter atendido suas dúvidas!\n')
        SairVoltar()
    elif opc == "6":
        print(f"\nNÚMERO {opc} DIGITADO.\nSUA DÚVIDA É -> 'O que fazer depois de concluir uma tarefa?'\n")
        divisoria()
        print("--SOLUÇÃO--")
        print("É muito simples! Para te ajudar na organização, o AgendEX📒 tem uma funcionalidade especial pra isso: ")
        print("-No Menu Inicial, digite a opção '3 - MARCAR TAREFA COMO CONCLUÍDA';")
        print("-Você podera escolher uma tarefa existente para marcar;")
        print("-Caso você não tenha criada nenhuma tarefa, o que impossibilita a marcação, uma mensagem será exibida notificando;")
        print("-Dessa forma, você diferencia tarefas já concluídas das tarefas que ainda precisam ser feitas.")
        print('Esperamos ter atendido as suas dúvidas!\n')
        SairVoltar()
    elif opc == "0":
        divisoria()
        print(f"\nNÚMERO {opc} DIGITADO.\nVOCÊ QUER -> 'Voltar ao menu inicial'\n")
        MenuInicial()
    else: 
        divisoria()
        print("A opção digitada não existe! Tente novamente.")
        divisoria()
        AjudaDuvidas()

def ListarTarefa():
    print("\n", " " * 18, "📘 LISTAR TAREFAS 📚", " " * 18, "\n") 
    print("BEM-VINDO(A), À SESSÃO DE LISTAGEM DE TAREFAS👋!")
    print("AQUI VOCÊ VÊ TODAS AS SUAS TAREFAS CRIADAS PARA FICAR\nSEMPRE POR DENTRO DE TUDO O QUE PRECISA FAZER E SE \nMANTER ORGANIZADO(A).")
    divisoria()
    if len(TarefasAgendex) > 0:
        print(" " * 18, "SUAS TAREFAS: ", " " * 18)
        for indice_tarefa, tarefa in enumerate(TarefasAgendex, start = 1):
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
            MarcarConcluida()
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


def MenuInicial():
    print(" " * 18, "MENU INCIAL", 18 * " ")
    print("Este é o menu inicial do AgendEX! 📒  \nAqui você acessa as principais funcionalidades do programa.\n")
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
        ListarTarefa()
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
        MensagemDeSaida()
    else:
        divisoria()
        print("\nERRO! OPÇÃO DIGITADA NÃO EXISTE ❌\n\n")
        MenuInicial()


divisoria()
print(" " * 18, "A-G-E-N-D-E-X", 18 * " ")
divisoria()
print("\nBem-vindo(a) ao AgendEX! 📒  \nAqui você organiza suas tarefas com facilidade.")
divisoria()
print("CONFIRME PARA ENTRAR NO AGENDEX 📒")
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
