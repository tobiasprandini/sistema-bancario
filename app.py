import os
import pwinput # Biblioteca para ocultar a senha ao digitar

# Variáveis globais para armazenar as credenciais (em um sistema real, isso seria armazenado de forma segura)
usuario_cadastrado = None
senha_cadastrada = None

saldo = 500 # Variável global para armazenar o saldo

def cadastrar_login():
    """
    Permite ao usuário cadastrar um novo login e senha.

    Retorna:
        tuple: Uma tupla contendo o nome de usuário e a senha cadastrados.
    """
    global usuario_cadastrado, senha_cadastrada

    print('--- Cadastro de Usuário ---')
    usuario_cadastrado = input('Digite um nome de usuário: ')
    senha_cadastrada = pwinput.pwinput('Digite uma senha: ')

    print('\nCadastro realizado com sucesso!\n')
    return usuario_cadastrado, senha_cadastrada

def login():
    """
    Realiza o login do usuário no sistema.

    Parâmetros:
        usuario_correto (str): O nome de usuário correto.
        senha_correta (str): A senha correta.

    Retorna:
        bool: True se o login for bem-sucedido, False caso contrário.
    """
    global usuario_cadastrado, senha_cadastrada

    if usuario_cadastrado is None or senha_cadastrada is None:
        print('Nenhum usuário cadastrado. Por favor, cadastre-se primeiro.\n')
        return False
    
    print('--- Login ---')
    nome_usuario = input('Digite o nome do usuário: ')
    senha = pwinput.pwinput('Digite sua senha: ')

    # Verifica se as credenciais estão corretas
    if nome_usuario == usuario_cadastrado and senha == senha_cadastrada:
        print('Login bem-sucedido!\n')
        return True # Login válido
    else:
        print('Informações inválidas. Tente novamente.\n')
        return False # Login inválido

def exibir_mensagem_incial():
    """Exibe a mensagem de boas-vindas ao usuário."""
    print('Seja bem-vindo ao seu banco preferido!\n')

def exibir_opcoes():
    """Exibe as opções disponíveis no menu principal."""
    print('1. Ver saldo')
    print('2. Saque')
    print('3. Depósito')
    print('4. Sair\n')

def escolher_opcoes():
    """Permite ao usuário escolher uma opção do menu e executa a função correspondente."""
    global saldo
    opcao_escolhida = input('Escolha uma opção: ')

    if opcao_escolhida == '1':
        exibir_saldo()
    elif opcao_escolhida == '2':
        realizar_saque()
    elif opcao_escolhida == '3':
        realizar_deposito()
    elif opcao_escolhida == '4':
        finalizar_app()
    else:
        print('Opção inválida. Tente novamente.\n')
        voltar_ao_menu_principal()

def exibir_saldo():
    """Exibe o saldo atual da conta."""
    global saldo
    print(f'Seu saldo é de R${saldo}\n')
    voltar_ao_menu_principal()
        

def realizar_saque():
    """Realiza um saque na conta, desde que haja saldo suficiente."""
    global saldo
    try:
        valor_saque = int(input('Digite o valor a ser sacado: R$'))
        if valor_saque > saldo:
            print('Saldo insuficiente para saque.\n')
        else:
            saldo -= valor_saque
            print(f'Saque realizado. Seu saldo é de R${saldo}\n')
    except ValueError:
        print('Valor inválido. Digite um número inteiro.\n')
    finally:
        voltar_ao_menu_principal()

def realizar_deposito():
    """Realiza um depósito na conta, desde que o valor seja válido."""
    global saldo
    try:       
        valor_deposito = int(input('Digite o valor a ser depositado: R$'))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'Depósito realizado com sucesso. Seu saldo é de R${saldo}\n')
        else:
            print('Digite um valor válido para depósito.\n')
    except ValueError:
        print('Valor inválido. Digite um número inteiro.\n')
    finally:
        voltar_ao_menu_principal()

def finalizar_app():
    """Finaliza o aplicativo."""
    os.system('cls')
    print('Sua sessão foi encerrada com segurança.\n')
    print('Obrigado por usar nosso app!')
    exit()

def voltar_ao_menu_principal():
    """Retorna ao menu principal após o usuário pressionar uma tecla."""
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def main():
    """Função principal que inicia o aplicativo."""
    os.system('cls')
    exibir_mensagem_incial()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    # Cadastro de usuário
    cadastrar_login()

    # Executa o login
    if login():
        while True:
            main()
    else:
        print('Acesso negado. Encerrando o aplicativo.')