import random
import os


print("Jogo da forca.")
print()

nome = input("Digite seu nome: ")
print(f"Olá, seja bem vindo {nome} ! Vamos começar a jogar?")
# Limpar mensagem de boas vindas, pra deixar o console limpo
input('\nPressione enter para começar')
# Limpa o console após a mensagem de boas vindas
os.system('cls')


# Aqui definir uma lista de palavra
lista_de_palavras = ['gato', 'chachorro', 'tigre', 'elefante']
# Guardei em uma variavél a palavra escolhida aleatória e com as letras tudo maiúsculo
palavras_selecionada = random.choice(lista_de_palavras).upper()
# Utilizei o método length(len) para ler o comprimento da palavra e salvei numa variavél
tamanho_palavra = len(palavras_selecionada)
# Coloquei numa lista de '_' o comprimento da palavra que vai ser escolhida
palavra_codificada = ['_']*tamanho_palavra
# Exibir a quantidade de erros do usuário
quantidade_de_erros = 0


# Defini um WHILE pra exibir que o jogo está em curso

# O jogo vai continuar em curso enquanto hover '_' na lista declarada
while '_' in palavra_codificada and quantidade_de_erros < 6:
    # Exibir o tamanho da palavra e qual o tema
    print(f'\nSua palavra tem {tamanho_palavra} letras, o tema é animais')
    # Exibir erros cometidos 
    print(f'Erros: {quantidade_de_erros} de 6')

    # Exibir a posição de cada letra que está na variavél (palavra_codificada)
    for letra in palavra_codificada:
        '''Exibir posição da letra. ex: ( _ _ _ _ _ ) por enquanto é só '_', após o usuário acertar a letra, 
        elá será exibida e subistituida. ex:( _ _ T _ _ )'''
        print(letra, end= ' ')
    print()
    
    # Resposta do usuário                          upper() Para deixar tudo maiúsculo, mesmo o usuário digitando em minúsculo
    letra_escolhida = input ('Digite uma letra: ').upper()
    # Caso a pessoa acerte a letra
    acertou = False
    # Lemos a paravra selecionado
    for i in range(len(palavras_selecionada)):
        # Comparamos se a letra escolhida for igual a palavra escolhida
        if letra_escolhida == palavras_selecionada[i]:
            # Faremos a subistituição pela letra escolhida
            palavra_codificada [i] = letra_escolhida
            acertou = True
    
    # Verificando se o usuário acertou a letra
    if acertou == True:
        print()
        print('Parabéns! Acertou.')
    else:
        print()
        print('Errou, essa letra não existe na palavra')
        # Se a letra não existir na palavra escolhida, quantidade de erros aumenta 1
        quantidade_de_erros = quantidade_de_erros + 1

# Verificando se o usuário atingiu a quantidades de erros de letras
if quantidade_de_erros == 6:
    print()
    print('Você perdeu! Boa sorte na proxima.')
else:
    print()
    print('Parabéns! Você ganhou.')
print()

# Caso o jogador perca, exibimos a palavra escolhida
print(f"A palavra era: {palavras_selecionada}")


# Cabo

    

    