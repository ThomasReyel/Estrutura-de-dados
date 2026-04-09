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

def funcB(n): #1
    i = 1 #1
    while i <= n: #(log2 n) + 1
        i = i*3 #log2 n
        print(i) #log2 n
funcB(8)
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

# def decimalBinario_01(n):
#     if n == 0:
#         return "0"
#     binario = ""
#     while n > 0:
#         resto = n % 2
#         binario = str(resto) + binario
#         n = n // 2
#         print(n)
#         print(binario)
#     return binario
# decimalBinario_01(8)

