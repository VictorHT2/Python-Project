import os

carros = ['McLaren F1','Nissan GTR','Bugatti']



def exibir_nome_do_programa():
    print("""
░█████╗░░█████╗░██████╗░██████╗░░██████╗  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
██║░░╚═╝███████║██████╔╝██████╔╝╚█████╗░  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██║░░██╗██╔══██║██╔══██╗██╔══██╗░╚═══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
╚█████╔╝██║░░██║██║░░██║██║░░██║██████╔╝  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")
def exibir_opcoes():
    print('1. Cadastrar carro')
    print('2. Listar carros')
    print('3. Escolher carro')
    print('4. Sair\n')
    
def finalizar_app():
    exibir_subtitulo('Finalizando o app')
    
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()
    
def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
 
def cadastrar_novo_carro():
    exibir_subtitulo('Cadastro de novos carros')
    nome_do_carro = input('Digite o nome do carro que deseja cadastrar: ')
    carros.append(nome_do_carro)
    print(f'O carro {nome_do_carro} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_carros():
    exibir_subtitulo('Listando os carros')
    
    for carro in carros:
        print(f'{carro}')
    
    voltar_ao_menu_principal()
    
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        

        if opcao_escolhida == 1: 
            cadastrar_novo_carro()
        elif opcao_escolhida == 2: 
            listar_carros()
        elif opcao_escolhida == 3: 
            print('Escolher carro:')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def main():
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()
    
if __name__ == '__main__':
    main()