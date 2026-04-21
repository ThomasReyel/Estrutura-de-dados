#Q1
#A) 2^n+ 4n² + 5n -> 2^n
#B) 3n² + 6 -> n²
#C) n³ + n² - n -> n³

#Q2
#Resposta: D

#Q3
# A)
# 3n² + 2n + 1 <= C n²
# (3n² + 2n + 1)/n² <= C
# 3 + 2/n + 1/n² <= C
# 3 + 2 + 1 <= C (assumindo n como 1)
# C = 3 n0 = 2
# 
# B)
# 3n + 6 <= C * n
# (3n + 6)/n <= C
# 3 + 6/n <= C
# C = 9 e n0 = 1
#
# C)
# n³ + n² - n <= C * n²
# n³ + n² - n NÃO É O(n²)

#Q4
# def funcA(n): 1
#     if n == 0: 1
#         print('Vazio') (Não entra no pior caso)
#     else: 1
#         for i in range(1,n+1): n+1
#             print(i) n
# 1+1+1+n+1+n
# 2n+4

# def funcB(n): #1
#     i = 1 #1
#     while i <= n: #(log2 n) + 1
#         i = i*3 #log2 n
#         print(i) #log2 n
# funcB(8)
# 3log n + 3 (talvez seja (3log2 n) + 6)

# def funcC(n):
#     i = n
#     while i > 0:
#         i = i//2
#         print(i)

# def funcD(n): #(1)
#     k = 1 #(1)
#     for i in range(1,2**n+1): #(2^n + 1)
#         if(2**k % i == 0):  #(2^n)
#             print(f"k = {i}") #(n+1)
#             k = k +1 #(n+1)
# funcD(4)
# 2*(2^n)+2n+5

#Q7
# def decimalBinario_01(n): 1
#     if n == 0: 1
#         return "0" 1 
#     binario = "" 1
#     while n > 0: # (log2 n) +1
#         resto = n % 2 (log2 n)
#         binario = str(resto) + binario (log2 n)
#         n = n // 2 (log2 n)
#         print(n)
#     return binario 1
# 4(log2 n) + 6
# decimalBinario_01(8)

#Q8
lista = [1,4,6,78,5,673,6,3,63,65,5,3,4,5,6,7,8,4]
listabin = [1,2,2,2,3,3,4,4,4,4,4,6,6,6,7]
def buscaListaSeq(lista, key): # 1
    posi = [] # 1
    for i in range(len(lista)): # n+1
        if key == lista[i]: # n
            posi.append(i)  # n
    return posi # 1
# 3n +4

def buscaListaBin(lista, key): # 1
    esq, dir = 0, len(lista) - 1 # 1 + 1
    primeiro = -1  # 1
    while esq <= dir: #(log2 n) +1
        meio = (esq + dir) // 2 #(log2 n)
        if lista[meio] < key: #(log2 n)
            esq = meio + 1 
        elif lista[meio] > key:
            dir = meio - 1
        else:
            primeiro = meio
            dir = meio - 1  
    if primeiro == -1: # 0
        return []  # 0
    esq, dir = primeiro, len(lista) - 1 # 1
    ultimo = primeiro # 1
    while esq <= dir: #(log2 n) + 1
        meio = (esq + dir) // 2 #(log2 n)
        if lista[meio] == key: #(log2 n)
            ultimo = meio
            esq = meio + 1  
        else:
            dir = meio - 1
    return list(range(primeiro, ultimo + 1)) #1
# 6(log2 n) + 8
print(buscaListaBin(listabin,4))