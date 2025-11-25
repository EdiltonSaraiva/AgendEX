print("_" * 49)
print("\n                  A-G-E-N-D-E-X                  \n")
print("_" * 49)

def divisoria():
    print("-" * 49)


print("___________________MENU INCIAL___________________\n")
print("Bem-vindo(a) ao AgendEX! 📝  \nAqui você organiza suas tarefas com facilidade.\n")
print("-Selecione uma opção abaixo:\n")
print("1️⃣  - ADICIONAR NOVA TAREFA.")
print("2️⃣  - LISTAR TAREFAS EXISTENTES.")
print("3️⃣  - MARCAR TAREFA COMO CONCLUÍDA.")
print("4️⃣  - EDITAR TAREFA.")
print("5️⃣  - REMOVER TAREFA.")
print("6️⃣  - SAIR DO SISTEMA.\n")

TarefasAgendex = []

opcao = (input("Por favor, digite o número da opção desejada: "))

if opcao == "1":
    print(f"\nOPÇÃO {opcao} SELECIONADA - ADICIONAR NOVA TAREFA")
    divisoria()
    print()
elif opcao == "2":
    print(f"\nOPÇÃO {opcao} SELECIONADA - LISTAR TAREFAS EXISTENTES")
    divisoria()
    print()
elif opcao == "3":
    print(f"OPÇÃO {opcao} SELECIONADA - MARCAR TAREFA COMO CONCLUÍDA")
    divisoria()
    print()
elif opcao == "4":
    print(f"\nOPÇÃO {opcao} SELECIONADA - EDITAR TAREFA")
    divisoria()
    print()
elif opcao == "5":
    print(f"\nOPÇÃO {opcao} SELECIONADA - REMOVER TAREFA")
    divisoria()
    print()
elif opcao == "6":
    print(f"\nOPÇÃO {opcao} SELECIONADA - SAIR DO SISTEMA")
    divisoria()
    print("\nSAIU DO PROGRAMA COM SUCESSO!\nOBRIGADO POR UTILIZAR.\n😁📴\n\n")
else:
    divisoria()
    print("\nERRO! OPÇÃO DIGITADA NÃO EXISTE ❌\n\n")
