f = open("large_scale/knapPI_1_200_1000_1", "r")

primeira_linha = f.readline()
# n numero de itens  w  capacidade da mochila 
n, w = primeira_linha.split()

pesos = []
valores = []

for i in range(int(n)):
    linha = f.readline()

    peso, valor = linha.split()

    pesos.append(int(peso))
    valores.append(int(valor))


#print(valores) # aqui 
#print(pesos) # aqui eu estou imprimindo todos os valores 
#print(peso)# aqui estou imprimindo um unico valor 


ultima_linha = f.readline()

itens_otimos = [bool(int(i)) for i in ultima_linha.split()]

print(itens_otimos) 



## teste  o que tive daqui para baixo pode ser considerado erro 
print("<",valores[0],valores[1])