from time import sleep
import random
import numpy as np
import string
import uuid
continuar = True
while continuar == True:
    sleep (0.5)
    print('MENU DE GERADOR DE SENHAS')

    menu= '''
    1 -> Senha de 4 números:
    2 -> Senha de 8 números:
    3 -> Senha de 8 números com letras minúsculas no final:
    4 -> Senha de 8 números com letras maiúscula no final:
    5 -> Senha de 8 números com letras minúscula e maiúscula no final:
    6 -> Senha de 8 letras aleatorias:
    7 -> Senha de 8 números e letras aleatorias:
    8 -> Gerar senha chave aleatoria identificadora universal exclusiva:
    '''
    print(menu)
    resposta_menu = int(input('Qual modelo de senha deseja ? ' ))

    if resposta_menu == 1:
        print('SENHA DE 4 DIGITOS')
        sleep(0.3)
        #Criar o array 1 x 1  com números aleatórios entre 1 e 9
        primeiro_menu = np.random.randint(0, 9, (1, 4))
        print(primeiro_menu)
    elif resposta_menu > 7:
        print('\033[1;31m''não existe esta opção no menu''\033[m')

    if resposta_menu == 2:
        sleep(0.3)
        print('SENHA DE 8 DIGITOS')
        #Criar o array 1 x 1  com números aleatórios entre 1 e 9
        segundo_menu = np.random.randint(0, 9, (1, 8))
        print(segundo_menu)

    if resposta_menu == 3:
        sleep(0.3)
        print('SENHA DE 8 DIGITOS COM LETRAS MINÚSCULAS')
        letras_minusculas_1 = chr(random.randint(ord('a'), ord('z')))
        letras_minusculas_2 = chr(random.randint(ord('a'), ord('z')))
        letras_minusculas_3 = chr(random.randint(ord('a'), ord('z')))
        letras_minusculas_4 = chr(random.randint(ord('a'), ord('z')))
        #Criar o array 1 x 1  com números aleatórios entre 1 e 9
        terceiro_menu = np.random.randint(0, 9, (1, 8))
        print(terceiro_menu, letras_minusculas_1, letras_minusculas_2, letras_minusculas_3, letras_minusculas_4)

    if resposta_menu == 4:
        print('SENHA DE 8 DIGITOS COM LETRAS MAIÚSCULAS')
        sleep(0.3)
        letras_maiusculas_1 = chr(random.randint(ord('A'), ord('Z')))
        letras_maiusculas_2 = chr(random.randint(ord('A'), ord('Z')))
        letras_maiusculas_3 = chr(random.randint(ord('A'), ord('Z')))
        letras_maiusculas_4 = chr(random.randint(ord('A'), ord('Z')))
        # Criar o array 1 x 1  com números aleatórios entre 1 e 9
        quarto_menu = np.random.randint(0, 9, (1, 8))
        print(quarto_menu, letras_maiusculas_1, letras_maiusculas_2, letras_maiusculas_3, letras_maiusculas_4)

    if resposta_menu == 5:
        sleep(0.3)
        print('SENHA DE 8 DIGITOS COM LETRAS MAIÚSCULAS E MINÚSCULAS')
        letras_minusculas_1 = chr(random.randint(ord('a'), ord('z')))
        letras_minusculas_2 = chr(random.randint(ord('a'), ord('z')))
        letras_maiusculas_1 = chr(random.randint(ord('A'), ord('Z')))
        letras_maiusculas_2 = chr(random.randint(ord('A'), ord('Z')))
        # Criar o array 1 x 1  com números aleatórios entre 1 e 9
        quinto_menu = np.random.randint(0, 9, (1, 8))
        print(quinto_menu, letras_minusculas_1, letras_maiusculas_2, letras_minusculas_2, letras_maiusculas_1)

    if resposta_menu == 6:
        sleep(0.3)
        print('SENHA DE LETRAS MAIÚSCULAS E MINÚSCULAS')
        letras_minusculas_1 = chr(random.randint(ord('a'), ord('z')))
        letras_minusculas_2 = chr(random.randint(ord('a'), ord('z')))
        letras_maiusculas_3 = chr(random.randint(ord('A'), ord('Z')))
        letras_maiusculas_4 = chr(random.randint(ord('A'), ord('Z')))
        letras_minusculas_5 = chr(random.randint(ord('a'), ord('z')))
        letras_maiusculas_6 = chr(random.randint(ord('A'), ord('Z')))
        letras_maiusculas_7 = chr(random.randint(ord('A'), ord('Z')))
        letras_minusculas_8 = chr(random.randint(ord('a'), ord('z')))
        print(letras_minusculas_1, letras_minusculas_2, letras_maiusculas_3, letras_maiusculas_4,
          letras_minusculas_5, letras_maiusculas_6, letras_maiusculas_7, letras_minusculas_8)

    if resposta_menu == 7:
        sleep(0.3)
        print('SENHA DE LETRAS E NÚMEROS ALEATÓRIOS')
        def random_generator(size=12, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        print(random_generator())

    if resposta_menu == 8:
        sleep(0.3)
        print('SENHA CHAVE ALEATÓRIA IDENTIFICADORA UNIVERSAL EXCLUSIVA')
        print(uuid.uuid4())

    sleep(1.5)
    recebe = int(input('\033[1;30m''Deseja fazer uma busca novamente:'
            '\033[m''\033[1;32m''\n 1 = (sim)''\033[m''\033[1;31m''\n'
            ' 2 = (não)''\033[m''\n''\033[1;30m''Qual das opções ? ''\033[m'))

    if recebe == 1:
        sleep(0.5)
        continuar = True
        print('\033[1;32m''ok iremos reiniciar nosso sistema''\033[m')
    if recebe == 2:
        sleep(0.5)
        continuar = False
        print('\033[1;31m''OK, muito obrigado por usar o nosso sitema nos agradecemos!!''\033[m')

