"""
faça uma lista de compras com listas
o usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
nao permita que o programa quebre com
erros de indices inexistentes na lista
"""
import os
compras = []

while True:
    select = input('Selecione uma opção\n(i)nserir (a)pagar (l)istar (s)air: ').lower()
    
    if len(select) > 1: #nao deixar usuario quebrar o programa
        os.system('cls')
        print('Digite somente uma opção')
        continue
    
    if select == '':
        os.system('cls')
        print('Nada digitado.')
        continue
    
    if select == 'i': #condiçoes para fazer as opçoes
        os.system('cls')
        inserir = input('O que deseja inserir?\n')
        compras.append(inserir)
        continue
    elif select == 'a':
        os.system('cls')
        for indice, nome in enumerate(compras):
            print(indice, nome)
        apagar = input('O que deseja apagar? ')
        
        #nao deixar usuario quebrar o programa por conta do indice
        try:
            indice = int(apagar)
            del compras[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
            
    elif select == 'l':
        os.system('cls')
        for indice, nome in enumerate(compras):
            print(indice, nome)
        continue
    elif select == 's':
        os.system('cls')
        sair = input('Quer sair? [s]im\n').lower().startswith('s')
        if sair is True:
            break
        else:
            continue
        
    
   