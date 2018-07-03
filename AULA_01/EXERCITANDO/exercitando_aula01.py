#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
2) Escreva um programa que calcule a temperatura em graus F. Lembre-se, o usuário forneceu a temperatura em graus C.

F = ((9 x C)÷5)+32
"""

C = float(input('Temperatura em C: '))
print('A temperatura em F é:',9*C/5+32)

"""
3) Um aluno deseja saber se foi aprovado na disciplina de Programação I. Para isso,
ele precisa tirar a média aritimética de suas duas notas, sendo que o resultado tem de ser maior ou igual a 6.
Do contrário, o aluno está reprovado.

MediaAritimética = (nota1 + nota2)/2
"""

nota01 = float(input('Nota 01: '))
nota02 = float(input('Nota 02: '))

print('Sua nota é:',(nota01+nota02)/2)


"""
4) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

kmPercorridos = float(input('Quantidade de km percorridos: '))
dias = int(input('Total de dias com o carro: '))


print('A pagar:\nkm Percorridos: R$ {}\nDias: R$ {}\nTotal: R$ {}'.format(kmPercorridos*0.15,dias*60,(dias*60+kmPercorridos*0.15)))

"""
5) Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer
e a velocidade média esperada para a viagem.
Vm = S/t
"""

S = float(input('Distância a percorrer: '))
vm = float(input('Velocidade média esperada para a viagem: '))
print('O tempo da viagem será de {} h.'.format(S/vm))




"""
Desenvolvido por Jackson Osvaldo da Silva Braga
GitHub: github.com/JacksonOsvaldo
E-mail: jacksonosvaldo@live.com
"""
