from pickle import TRUE


f = open("large_scale/knapPI_1_200_1000_1", "r")

primeira_linha = f.readline()
# n numero de itens  w  capacidade da mochila 
n, w = primeira_linha.split()

pesos = []
valores = []
pesosOtimos =[]
valoresOtimos =[]
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

# print(">",itens_otimos) imprimir os boolean  






## tudo certo . ultimo commit feito 12:00 30/06/2022
print("<",valores[0],valores[1])

print(type(itens_otimos[0]))

carro =True
if carro ==True:
    print("Bum")



## segunda implementação tudo certo .O algorimto atende o que foi requisitado .
for i in range(int(n)):
    
   # print(itens_otimos[i])
    if itens_otimos[i]==True:
        #print("VVV",[i])#16 no total com true . verificando se o elemento foi inserido no if
        pesosOtimos.append(pesos[i])
        valoresOtimos.append(valores[i])


print("Imprimindos os pesos dos valores que foram inseridos na mochila\n ",pesosOtimos)
print("Imprimindos os valores que foram inserido na mochila\n",valoresOtimos)

## terceira implementação .Periodo de teste 
##  objetivo fazer a soma dos valores dos pesosOtimos e valoresOtimos 


somaDosPesos=0

capacidadeMax =int(w)
"""
#soma dos pesosOtimos
for i , num in enumerate(pesosOtimos):

#for i in range(pesosOtimos):
    somaDosPesos = somaDosPesos+pesosOtimos[i]
    print(somaDosPesos)
    if( somaDosPesos>=capacidadeMax):
        somaDosPesos = somaDosPesos - pesosOtimos[i]
    
"""
    
 

for i , num in enumerate(pesos):

#for i in range(pesosOtimos):
    somaDosPesos = somaDosPesos+pesos[i]
    
    if( somaDosPesos>=capacidadeMax):
        somaDosPesos = somaDosPesos - pesos[i]
    


print(pesos)
print("pesoBom",somaDosPesos)
print("pesosOtimos",pesosOtimos)
print(w) #w  é a capacidadeDa mochila
print(n) #n  e o numeros de itens 


"""
def somaW (pesosOtimos,w):

    capacidadeMax=int(w)
    somaDosPesos=0
    for i , num in enumerate(pesosOtimos):
        
        #for i in range(pesosOtimos):
        somaDosPesos = somaDosPesos+pesosOtimos[i]
        print(">>",somaDosPesos)
        if( somaDosPesos>=capacidadeMax):
            somaDosPesos = somaDosPesos - pesosOtimos[i]

    return   somaDosPesos


somaW(pesos,w)
    """