# def fatorial(n): #1
#     fator = 1 #1
#     if n > 0:
#         # n
#         fator = n * fatorial(n-1) #(n-1) +@(1)    obs: @ é teta
#     return fator
# print(fatorial(5))

def impr(n):
    if n == 1:
        print(n)
    else:
        print(n)
        impr(n-1)

impr(5)