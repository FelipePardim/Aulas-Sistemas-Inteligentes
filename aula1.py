#definição de variaveis
a = 3
b = 2
c = a
d = "Clube do Remo"

#imprimindo
print("imprimindo var:", d)

if a == b:
 print("True")
elif a != b:
 print("Encadeado")
else:
 print("False")

#estrutura de repeticao
for i in d:
 print(i)

#estrutura de repeticao
for i in range(1,10):
 print(i)

#lista
lista = [1,2,3,4,5,6]
print(lista)

for index, elemento in enumerate(lista):
 print(index, ":", elemento)

#funcoes
def soma(x, y):
 result = x + y
 return result

def imprimir_relatorio(relatorio):
 print("relatorio :", relatorio)

r = soma(5,5)
imprimir_relatorio(r)