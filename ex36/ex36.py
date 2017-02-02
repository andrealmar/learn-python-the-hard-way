# -*- coding: utf-8 -*-
from sys import exit

"""
PORTA DOS DESESPERADOS - THE GAME
"""

print "rá iéié meu gluglu"
print "você está desesperado?"
resposta = raw_input("> ")

if resposta == "sim":
    print "Então vamos começar o jogo...!!!"
else:
    print "Se você não está desesperado o que você está fazendo aqui?"
    exit(0)


def porta_1():
    print "Você abriu a porta número 1"
    print "Um URSO saiu da porta número um e te devorou!!!"
    print "GAME OVER!!!"


def porta_2():
    print "Você abriu a porta número 2"
    print "Você ganhou um chiclete...!!!"
    print "Não é um prêmio tão bom assim, mas melhor que nada ne...."


def porta_3():
    print "Você abriu a porta número 3"
    print "Tem um Macbook lá dentro!!!!"
    print "PARABÉNS VOCÊ GANHOU UM MACBOOK. RETIRE O SEU PRÊMIO!!!"


def start():
    print "Escolha a PORTA: "
    choice = raw_input("> ")

    if choice == "1":
        porta_1()
    elif choice == "2":
        porta_2()
    elif choice == "3":
        porta_3()
    else:
        print "Você não escolheu nenhuma porta. Recomece o JOGO"


start()
