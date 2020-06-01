"""
Algarismos de menor ou igual valor à direita são somados ao algarismo de maior valor;
Algarismos de menor valor à esquerda são subtraídos do algarismo de maior valor.
"""
nums = {'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1}
cont = 0
result = 0


def VerificaInput(valor_romano):
    for cont in valor_romano:
        if cont not in 'MDCLXVI':
            return True
        else:
            return False

def traduz_input(valor_romano):
    global valor_romano_list
    valor_romano_list = []

    for c in valor_romano:
        valor_romano_list.append(nums[c])


valor_romano = input("Digite um numero romano: ").upper()

VerificaInput(valor_romano)

if valor_romano == "" or VerificaInput(valor_romano) == True:
    while valor_romano == "" or VerificaInput(valor_romano) == True:
        valor_romano = input("\nINVÁLIDO!!\nDigite um numero romano: ").upper()
        VerificaInput(valor_romano)

traduz_input(valor_romano)

if len(valor_romano) == 1:
    print(nums[valor_romano])

else:
    cont = 0
    valores_analisados = []
    while cont < len(valor_romano_list):
        if cont not in valores_analisados:

            #Algarismos de menor ou igual valor à direita são somados ao algarismo de maior valor;
            try:
                if valor_romano_list[cont] >= valor_romano_list[cont + 1]:
                    result += (valor_romano_list[cont] + valor_romano_list[cont + 1])
                    valores_analisados.append(cont)
                    valores_analisados.append(cont+1)
                    cont += 1
                    continue
            except IndexError:
                if valor_romano_list[cont] <= valor_romano_list[cont - 1]:
                    result += valor_romano_list[cont]
                    valores_analisados.append(cont)
                    valores_analisados.append(cont-1)
                    cont += 1
                    continue

        #Algarismos de menor valor à esquerda são subtraídos do algarismo de maior valor.
            if valor_romano_list[cont - 1] < valor_romano_list[cont]:
                result += (valor_romano_list[cont]-valor_romano_list[cont - 1])
                valores_analisados.append(cont)
                valores_analisados.append(cont - 1)
        cont += 1
print(result)