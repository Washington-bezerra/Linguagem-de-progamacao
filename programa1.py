'''
#########################################################
#Created by: Thiago da Silva Moyses                     #
#RA: 1811515099                                         #
#Course: electrical engineering                         #
#GitHub: http://github.com/thiagomoyses                 #
#-------------------------------------------------------#
#created by: Washington Luis Santos Bezerra             #
#RA: 1811512370                                         #
#Course: computer engineering                           #
#GitHub: http://github.com/washington-bezerra           #
#-------------------------------------------------------#
#Last Update: 2020/04/05                                #
#########################################################
'''
#Instruçoes
print("############################## INSTRUÇOES ##############################")
print("# 1) Digite apenas numeros Inteiros                                    #")
print("#----------------------------------------------------------------------#")
print("# 2) Não digite letras ou simbolos                                     #")
print("#----------------------------------------------------------------------#")
print("# 3) Caso nao queira inserir mais numeros, Basta Digitar a letra N     #")
print("#----------------------------------------------------------------------#\n\n")
##Variavel que receberá os numeros digitados
lista = []
#while usado para que o usuário possa inserir quantos numeros desejar
while True:
	#variavel que recebe o numero inserido
	numero = input("Digite algum numero ->  ")
	if(numero == "n") or (numero == "N"):
		break
	else:
		try:
			lista.append(int(numero))
		except:
			print("Digite um valor Valido! Leia as instruçoes.")
#funçao para somar os valores da lista
def soma(lista):
	#iniciando variavel de resultado
	result_soma = 0
	#percorrendo lista e somando
	for count in lista:
		result_soma += count
	return result_soma
#funçao para somar os valores pares
def somapar(list):
	#iniciando variavel de resultado
	result_par = 0
	#percorrendo Lista e somando
	for count in lista:
		#Testando se o numero é par ou impar, e caso par, atribuindo a soma
		if count % 2 == 0:
			result_par += count
	return result_par
##funçao para somar os valores impares
def somaimpar(ls):
	#Iniciando variavel de resultado
	result_impar = 0
	#percorrendo lista e somando
	for count in lista:
		#Testando se o numero é impar, caso impar, atribuindo a soma
		if count % 2 != 0:
			result_impar += count
	return result_impar
#lista de numeros digitados
print("######################### RESULTADO DAS OPERAÇOES #########################\n\n")
print("*Numeros Digitados:  ", lista)
print("---------------------------------------------------------------------------")
#ordenando e printando por ordem crescente
lista.sort(key=int)
print("\n*Numeros em ordem crescente:  ", lista)
print("---------------------------------------------------------------------------")
#ordenando e printando por ordem decrescente
lista.sort(key=int, reverse=True)
print("\n*Numeros em ordem decrescente: ", lista)
print("---------------------------------------------------------------------------")
#Printando soma de todos os valores
print("\n*Soma de todos os valores da Lista: ",soma(lista))
print("---------------------------------------------------------------------------")
#Printando soma de valores pares
print("\n*Soma de todos os valores pares da Lista: ",somapar(lista))
print("---------------------------------------------------------------------------")
#Printando soma de valores impares
print("\n*Soma de todos os valores impares da Lista: ",somaimpar(lista))
print("---------------------------------------------------------------------------")