#List Comprehension
"""lista=[11,21,31]

novaLista = [item *2 for item in lista]
print(novaLista)

novaLista = [item  for item in lista if item >=20 ]
print(novaLista)
"""

#Reduce
"""
Reduce não tem no pacote deve ser importado 
***
from functools import reduce
***

from functools import reduce

lista=[11,21,31]
acumula = 0 
for item in lista:
    acumula = acumula + item
print(acumula)

funcao = lambda acumulador , item: acumulador + item
resultados = reduce(funcao , lista ,10)
print(resultados)
"""


#Filter
"""
lista=[11,21,31]
novaLista = filter(lambda n:n >=20, lista)
print(list(novaLista))

lista = [
    {'produto':'Fone','preco':500},
    {'produto':'Telefone','preco':300},
    {'produto':'Som','preco':700},
    {'produto':'Iphone','preco':200},
]

novaLista = filter( lambda p : p["preco"] >= 400 , lista )
print(list(novaLista))
"""


#Map
""""
lista=[11,21,31]
listanove = map( lambda n: n*2,lista)
l = list(listanove)
print(l)

lista = [
    {'produto':'Fone','preco':500},
    {'produto':'Telefone','preco':300},
    {'produto':'Som','preco':700},
    {'produto':'Iphone','preco':200},
]

novaLista = map(lambda p: p["preco"] *2, lista)
print(list(novaLista))

def calcularmutiplo(produto):
    produto["preco"]= produto["preco"] * 2
    return produto

novaLista = map(calcularmutiplo, lista)
print(list(novaLista))
"""


#Função de ordem superior
"""
def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

lista = [somar,subtrair]
for funcao in lista:
    print(funcao(1,2))
"""


#Função
"""
def calcular(nome,n1,n2,n3):
    print(f'O aluno {nome} a media do ano letivo é : {(n1+n2+n3)/3}')
calcular('igor',10,9,8)
"""


#Estrutura de Repetição
"""
while Condição:
    print()
    Condição++
***Voce entendeu 

    break
***Quebra o fluxo da execução

    continue
***Contina com o fluxo da condição mas não executa o resto do código

for valor in Variavel:
    print()

***For um python é um map do js

"""


#Concatenação de texto
"""
Carateristica = 'Bonito'
print('Eu sou'+Carateristica)

print('Nome: %s, Preco> %d' % (Nome,Preco))
Substitui o parametro na stris pelo valor da variavel

%s String
%d Number
%f Float

print('Nome: {}, Preco> {}' % (Nome,Preco))
Mesma coisa

print('Nome:{Valor}, preco:,{Valor}')
Maneira simples
"""


#Dicionarios e conjuntos
"""
dicionarios ={
    'correr':'anda',
    'parar': 'stop',
    'idade': 34,
    'array':["",""],

A estrutura do dicionario cria um valor para determinado parametro cujo seu valor é 
declarado quando a chave é chamada, os : pontos separam a chave (Id) do valor 
}

print(dicionario['idade'])
Chamado indice da lista

dicionario['km'] = 8500
Estou adicionando mais um indice no dicionario

dicionario['array'].append("")
Adicionando um indice no final do array

dicionario['km'] =  8000
Definindo uma nova string para valor existente

del dicionario['km']
Deleta o indice definido 

dicionario.keys()
Mostra os itens das listas

dicionario.values()
Retorna a lista com seus id e valores
"""


#Tuplas
"""
         0  1  2  3
Lista = ("","","","")
Uma tupla é uma lista só que ela é imutavel
"""


#Listas ou Array
"""
Mutavel, dinamica, heterogenea e indexada 
         0  1  2  3
Lista =["","","",""]

*** Alterar o valor
Lista[Local] =  ""

*** Adicionando um Valor ao final da lista
Lista.append("")

*** Removendo Iten da lista
Lista.remove("")
Remove determinado item ou valos da lista 

del Lista[2]
Remove o determinado valor declaradon os parametros de string podem ser conbinados
del Lista[2:5]

Lista.count("")
Essa funçao conta a quantidade de parametro declarada que tem lista 

Lista.clear()
Limpa a lista

Lista.revers()
Inverte a Ordem 

Lista.sort()
Ordena de acordo com a alfabeto
"""


#Metodos
"""
dir(Valor)
***Mostra todos os metos do valor
"""


#Operadores com text0 
"""
Texto = 'Meu nome é igor'

print('igor' in Texto)
print('igor' not in Texto)
*** In OU Not In Retorna Um valor Boolean True ou False se determinado parametro esta na String

print(len(Texto))
*** Retorna um nunber contando a quantidade de caracteres na String

print(Texto.lower())
Deixa a string Minuscula
print(Texto.upper())
Deixa a string Maiuscula
"""


#Operações com Strig
"""
Quebra de linha \n

Text = 'Seu carro é muito bom'

print(text[4]) 
Essa função retorna o local da determinada da strig

print(text1[-5])
Essa função retona a possição de trais pra frente 

print(2:5)
Determina o inicio e o final, retornando uma string entre os valores 

print(::3)
Pula a quantidade de carracters determinada o ultimo valor
"""

#Função
"""
**type() 
Retorna o type do valor

**int('str')
Converte um valor Str para Number 

**string('number')
Converto uma Number para String

**float('number, string')
Converte para Float
"""


#Operador Ternário
"""
('False','True')[Condição]
"""


#Estruturas Condionais 
"""
if Condicao:
    print()
elif Condicao:
    print()    
else:
    print()
"""


#Operadores Logicos e Relacionais
""" 
*** Relacionais ***
Igualdade ==
Diferente !=
Maior Q >
Menor Q <
Maior ou Igual >=
Menor ou Igual <=

__ Retorna Um valor Boolean Falso ou True __

*** Logicos ***

and (e)
Os dois valores devem retornas True

or (ou)
Um dos Valor devem retornar True
"""


#Operadores aritimeticos
"""
Subtração (-)
Adição (+)
Dividir (/)
Multiplicação (*)
Exponenciação (**)
Módulo (%) Resto da divisão

Valor ++  
Valor -= (Valor)
Valor += (Valor)
Valor /+ (Valor)

___Precedencia___

    * / + - 



"""


#Tipos de dados
"""
Python tem variaveis dinamicas não prescisa definir 
"""

# Chamada de função 
"""
def executar():
    print("")

executar();
"""