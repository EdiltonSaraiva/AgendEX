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



    # PARTE DO SISTEMA TO-DO -DELETA (REMOVER) TAREFA
# obs: para o uso dessa fução precisa integrar com os sitema principal mais abaixo tem exemplo de aplicação (codigo teste)

'''
observação: Esta função deletar_tarefa usa a variável uma global que 
tambem faz parte do codigo principal, (listar_tarefas) caso a declaração 
dessa varivel seja divergente desse codigo deve ocorrer alteração  
'''


def deletar_tarefa():
    '''
    essa é Função responsável por deletar/remover uma tarefa da lista
    O que esta função faz? 
    1. Verifica se existem tarefas para deletar
    2. Mostra a lista de tarefas disponíveis
    3. Pede ao usuário o número da tarefa
    4. Valida a entrada do usuário
    5. Remove a tarefa da lista
    6. Exibe mensagem de confirmação
    obs: algumas coisas podem ser mudada ao decorrer do processo do codigo
    '''

  # Imprime o cabeçalho da seção de deletar tarefa
    print("\n" + "-"*50)
    print("         DELETAR TAREFA")
    print("-"*50)

    # 1- aqui baixo vai Verificar se existem tarefas na lista
    # Usando o len() para contar quantas tarefas existem
    # Se for 0 (zero), significa que a lista está vazia

    if len(listar_tarefas) == 0:
        print("\nNão há tarefas cadastradas para deletar!")
        # decrição para  o usuario alteravel corforme o menu
        print("ATENÇÃO! para deletar uma tarefa, Adicione tarefas primeiro, usando a opção 2 do menu principal.")
        return  # Encerra a função aqui, não há nada para fazer

     # 2 - Mostrar todas as tarefas disponíveis
    print("\n suas Tarefas cadastradas são: ")
    print("-" * 50)

    ''''
    aqui a baixo Percorre a lista de tarefas para exibir cada uma
    enumerate() retorna o índice (posição) e o item (tarefa)
    O índice começa em 0, porem, mostrar para o usuario começando em 1.
    '''

    for indice_lista, tarefa in enumerate(listar_tarefas):

        # Calcula o número que será mostrado ao usuário
        # Somamos 1 porque o usuário entende melhor numeração de 1 a N... etc
        numero_para_usuario = indice_lista + 1

        # essa parte  Pega a descrição da tarefa (está na posição 0 da lista)
        descricao_da_tarefa = tarefa[0]

        # já essa parte Pega o status da tarefa (está na posição 1 da lista)
        status_da_tarefa = tarefa[1]

        #
        print(
            f"{numero_para_usuario}. [{status_da_tarefa.upper()}] {descricao_da_tarefa}")

        # Mostra quantas tarefas existem no total
    # de forma hipotetica essa parte quantos as demais pertes com essa variavel usar variavel da função listar tarefas do programa
    total_de_tarefas = len(listar_tarefas)
    print("-" * 50)
    print(f"Total de tarefas no AgendEX: {total_de_tarefas}")

    # Pedir ao usuário qual tarefa deletar
    print("\n")
    numero_digitado_pelo_usuario = input(
        "Digite o número da tarefa que você deseja deletar do seu AgendEx: ")

    # essa parte vai fazer VALIDAÇÕES - Verificar se o que o usuário digitou é válido

    # VALIDAÇÃO  1 : Verifica se o usuário digitou apenas números
    # isdigit() retorna True se todos os caracteres forem números (0-9)
    # Retorna False se tiver letras, espaços ou caracteres especiais
    if not numero_digitado_pelo_usuario.isdigit():
        print("\nXXX ERRO: Você precisa digitar apenas números!")
        print("Exemplo: Para deletar a tarefa 1, digite: 1")
        return  # Encerra a função se a entrada for inválida

     # VALIDAÇÃO 2: Converte o texto para número inteiro
    # pois, Agora sabemos que é um número válido, então essa parte vai  converter para um valor inteiro e armazenar na variavel
    numero_da_tarefa_escolhida = int(numero_digitado_pelo_usuario)

    '''
    VALIDAÇÃO 3: Calcula o índice real na lista
    O usuário vê tarefas numeradas como: 1, 2, 3, 4... etc
    porém a lista em ython usa índices de: 0, 1, 2, 3...etc
    Por isso, subtraímos 1 do número digitado 
    '''
    indice_real_na_lista = numero_da_tarefa_escolhida - 1

    # VALIDAÇÃO 4: Verifica se o número da tarefa existe
    # O índice não pode ser negativo por exemplo: (menor que 0)
    # O índice não pode ser maior ou igual ao tamanho da lista
    if indice_real_na_lista < 0:
        print(
            f"\nXXX-ERRO: ATENÇÃO !!! esse número [{numero_da_tarefa_escolhida}] é inválido!")
        print("POR FAVOR, DIGITE UM NÚMERO VALIDO.")
        return

    if indice_real_na_lista >= len(listar_tarefas):
        print(
            f"\nXXX-ERRO: ATENÇÃO !!! A tarefa de número [{numero_da_tarefa_escolhida}] não existe!")
        print(
            f"Você tem apenas {len(listar_tarefas)} tarefa(s) cadastrada(s).")
        return

    # parte de  Deletar ou remove a tarefa
    # Antes de deletar, vamos guardar a descrição para mostrar ao usuário
    descricao_da_tarefa_deletada = listar_tarefas[indice_real_na_lista][0]

    # Agora sim, remove a tarefa da lista usando pop()
    # pop(índice) remove o item na posição especificada e retorna ele
    listar_tarefas.pop(indice_real_na_lista)

    # Confirmação da exclusão para o usuário
    print("\n" + "-"*50)
    print("TAREFA DELETADA COM SUCESSO DO AgendEX!")
    print("-"*50)
    print(f"A TEREFA REMOVIDA DO AgendEX FOI: {descricao_da_tarefa_deletada}")
    print(f"AS TAREFAS RESTANTES SÃO: {len(listar_tarefas)}")

    # EXEMPLO DE USO E TESTE DA FUNÇÃO


# Este código abaixo serve para APENAS testar a função  DE FORMA isoladamente
# No código principal do grupo NA  BRANCH (MAIN),  não precisa deste exemplo baixo
if __name__ == "__main__":

    print("="*50)
    print("  TESTE DA FUNÇÃO DELETAR TAREFA")
    print("="*50)
    print("\nCriando tarefas de exemplo para testar...")

    # Cria uma lista de tarefas de exemplo
    listar_tarefas = [
        ["Estudar Python", "pendente"],
        ["Fazer trabalho de matemática", "pendente"],
        ["Revisar código do projeto", "concluída"],
        ["Ler documentação", "pendente"]
    ]

    print(f" {len(listar_tarefas)} tarefas criadas!")

    # Chama a função para testar
    deletar_tarefa()

    print("\n" + "="*50)
    print("FIM DO TESTE")
    print("="*50)

