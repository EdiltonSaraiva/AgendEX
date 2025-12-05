def divisoria():
    print("-" * 49)


def AjudaDuvidas():
    def SairVoltar():
        divisoria()
        print('Deseja FECHAR O PROGRAMA ou VOLTAR AO MENU INCIAL?')
        print('1 - VOLTAR AO MENU INICIAL.')
        print('2 - FECHAR O PROGRAMA AGORA.')
        divisoria()

        opc = input("Digite aqui o NÚMERO da opção desejada: ")

        if opc == "1":
            MenuInicial()
        elif opc == "2":
            divisoria()
            print("\nSAIU DO PROGRAMA COM SUCESSO!\nOBRIGADO POR UTILIZAR.\n😁📴\n\n")
        else: 
            divisoria()
            ("A opção digitada não existe! Por favor, tente novamente.")


    print("\n", " " * 18, "❓AJUDA E DÚVIDAS🤔", " " * 18 , "\n") 
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
        print("-Em seguida, você deve confirmar a exlcusão no menu, com a opção '1 - SIM, DESEJO EXLUIR';")
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
        AjudaDuvidas()


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
    AjudaDuvidas()
elif opcao == "7":
    print(f"\nOPÇÃO {opcao} SELECIONADA - SAIR DO SISTEMA")
    divisoria()
    print("\nSAIU DO PROGRAMA COM SUCESSO!\nOBRIGADO POR UTILIZAR.\n😁📴\n\n")
else:
    divisoria()
    print("\nERRO! OPÇÃO DIGITADA NÃO EXISTE ❌\n\n")
