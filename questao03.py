import math
num: int
quad: int 
raiz: int
cubo: int
linha: int

num = int(input("Digite um número: "))
quad = num * num
cubo = num * num * num
linha = 1
raiz = math.sqrt(num)

while linha < 20:
    linha = linha + 1
    print(f"Número: {num}; Quadrado: {quad}; Cubo: {cubo}; Raiz: {raiz:.2f} ")

