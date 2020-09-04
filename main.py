#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import statistics

def valores():
    n = int(input("Informe o tamanho do conjunto númerico: "))
    i = 0
    lista = []

    for i in range(n):
        lista.append(float(input("Número: ")))

    lista = sorted(lista)
    return lista

def media_aritmetrica():
    n = valores()
    x = sum(n) / len(n)
    x = round(x, 2)
    print("A media aritmetrica desse cunjunto eh: ", x)

def media_ponderada():
    n = int(input("Informe o tamanho do conjunto númerico: "))
    i = 0
    y = 0
    z = 0
    a = 0

    for i in range(n):
        dados = float(input("Número: "))
        pesos = float(input("Peso: "))
        a += dados
        y += (dados*pesos)
        z += pesos
        i += 1
        
    try:
        x = float(y/z)
        x = round(x, 2)
        print("A media ponderada desse conjunto eh: ", x)
    except ZeroDivisionError:
        x = a/n
        print("A media desse conjunto eh: ", x)

def moda():
    n = valores()

    try:
        x = statistics.mode(n)
        print("A moda desse conjunto eh: ", x)
    except statistics.StatisticsError:
        print("\n <|||> ERRO: conjunto Amodal (sem moda) <|||> ")

def mediana():
    n = valores()
    x = statistics.median(n)
    print("A mediana desse conjunto eh: ", x)

def main():			# Função principal, montado com as funções anteriores...
    i = True
    
    print("""
		=======================================================
		||           <<<===>>> Medidas <<<===>>>             ||
		||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
		||            <<<===>>> de <<<===>>>                 ||
		||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
		||      <<<===>>> Tendencia Central <<<===>>>        ||
		=======================================================
	 """)
    
    while(i == True):
        print("\n	Informe o número correspondente para a opção desejada: ")
        print("	(1) Calcular media aritmetrica;")
        print("	(2) Calcular media ponderada;")
        print("	(3) Calcular moda;")
        print("	(4) Calcular mediana;")
        print("	(0) Para Encerrar;")
        op = int(input(">>> "))
        
        if(op < 0) or (op > 5):			# Caso a opção informada seja invalida
            print("\n <|||> ERRO: opção invalida... <|||> \n  **Por favor, reinicie o programa e imforme uma opção valida...")
            exit()
            
        elif(op == 1):
            media_aritmetrica()
            
        elif(op == 2):
            media_ponderada()
            
        elif(op == 3):
            moda()
            
        elif(op == 4):
            mediana()
            
        elif(op == 0) or (i == False):	# Encerra o programa
            print("	Obg por usar nossa Calculadora! ")
            print("				< by Alunos do 3º'I' 2019 > ")
            break

main()
