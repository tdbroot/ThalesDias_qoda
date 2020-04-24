#Thales Dias
print("\n\nThales Dias thales89dias@gmailcom. Exercícios em Python dia 01. QODA TECNOLOGIA.\n")
input("Vamos lá! Aperte Enter para INICIAR.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DESAFIO PYTHON
print("\n\nTAREFA 1: Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58\n")
alt = float(input ("Qual é a sua altura?\n"))
peso = ((72.7*alt)-58)
print(f"Seu peso ideal é: {peso}\n")

input("Aperte Enter para continuar...")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DESAFIO CONDICIONAIS
print("\n\nTAREFA 2: Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem Bom Dia!, Boa Tarde! ou Boa Noite! ou Valor Inválido!, conforme o caso.\n")
periodo=input("Escolha o turno desejado. Utilize:\n'M'para matutino. 'V' para vespertino. 'N' para noturno.\n")
if periodo == "M":
	print("\nOlá, bom dia!\n")
elif periodo == "V":
	print("\nBoa tarde!\n")
elif periodo == "N":
	print("\nTenha uma boa noite!\n")
else: 
	print("\nErro!Valor Inválido.\n")

input("Aperte Enter para continuar...")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#DESAFIO REPETIÇÃO
print("\n\nTAREFA 3: A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.\n")
pause = int(input("Entre com o número desejado para visualizar a sequência de Fibonacci:\n"))
print('\n A sequência de Fibonacci para o número',pause,'é:\n')
bf = 0
af = 0
while (af<pause):
	af = af + bf
	bf = af - bf
	if af == 0:
		af = af+1
	print (af,'\n')

input("Aperte Enter para continuar...")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DESAFIO FUNÇÕES
print("\n\nTAREFA 4: Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.\n")
#Declarando a função 'switch'
def switch(x):
	return x[::-1]
#Declarando a varíavel 'val', que receberá um input do usúario.
val=input("Entre com o valor para ser invertido.\n")
#Chamando a função 'switch'
val_invert=switch(val)
#Apresentando resultado na tela.
print('Este valor invertido é:',val_invert,'\n')

input("Fim do exercício QODA TECNOLOGIA. Aperte Enter para SAIR...")

