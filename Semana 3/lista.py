def main():
    # Questão 1 c)
    # Questão 2 a) c) d) b)
    # Questão 3 d)
    # Questão 4
    # Na análise empírica, você necessita execultar o código em diversas circustâncias para contabilizar
    # o tempo de execulção de cada uma, o que pode ser um problema para códigos que não podem ser
    # execultados tão facilmente. Já a análise matemática, ela cria representações matemáticas
    # que permitem ver qual código é menos complexo.
    # Questão 5
    # Na memória do PC existe uma área reservada para as instruções que o computador deve realizar,
    # Então ele vai percorrendo essa secção (sempre incrementado +1 para o contador) então ele recebe
    # a instrução, decodifica ela e a executa, então incrementa mais 1 no contador e repete o processo
    # "infinitamente"
    # Questão 6
    # a) 1
    # b) 1
    # c) 3
    # d) 3
    # e) 5
    # Questão 7: d) c) a) e) b)

    # Questão 8
    # def somar(a, b): 1
    #     soma = a + b 2
    # return soma 0
    # t(n) = 3

    # def multiplicar(a, b):
    #     produto = a * b
    #     return produto
    # t(n) = 4

    # def potencializar(b, e): (1)
    #     potencia = 1 (1)
    #     for i in range(e): (e + 1)
    #         potencia *= b (e)
    #     return potencia (1)

    # t(e) = 2e + 4

    #Questão 9
    # def somar(a, b): 1
    #     soma = a + b 2
    #     return soma 0
    # t(n) = 4 No caso anterior o returno não execultava por conta da sua identação ele estava errado

    # def multiplicar(a, b): (1)
    #     produto = 0 (1)
    #     for i in range(b): (b + 1)
    #         produto = somar(produto, a) (b)
    #     return produto (1)
    # t(b) = 2b + 4 Nesse caso como existe um for, ele sempre execultará b vezes + 1 e dentro dele apenas b vezes

    # def potencializar(b, e):
    #     potencia = 1
    #     for i in range(e):
    #         potencia = multiplicar(potencia, b)
    #     return potencia
    # t(e) = 2e + 4 

    # Questão 10 (len(texto) = n)
    # def num_consoantes(texto): (1)
    #     count = 0 (1)
    #     for i in (texto): (n +1)
    #         if i != "a" and i != "e" and i != "i" and i != "o" and i != "u": (n)
    #             count += 1 (n)
    #     return count (1)
    # t(n) = 1 + 1+ n+1 + n + n + 1
    # t(n) = 3n + 4

    # Questão 13
    #Versão 1 (len(lista2) = n)
    # def união(lista01, lista02): (1)
    #     lista03 = lista01 (1)
    #     for i in lista02: (n+1)
    #         if i not in lista03: (n)
    #             lista03.append(i) (n)
    #     return lista03 (1)
    # t(n) = 3n + 4

    # Versão 2
    # def união(lista01, lista02): (1)
    #     lista03 = set(lista01) (1)
    #     lista03.update(lista02) (1)
    #     return lista03 (1)
    # t(n) = 4

    # Questão 14
    # def ordenar(lista): (1)
    #     n = len(lista) (1)
    #     for i in range(n): (n+1)
    #         for j in range(0, n-i-1): (n . (n+1))
    #             if lista[j] > lista[j+1]: (n.n)
    #                 lista[j], lista[j+1] = lista[j+1], lista[j] (n . n)
    #     return(lista) (1)
    # t(n) = 1+1+(n+1)+(n.(n+1))+(n.n)+(n.n)+1
    # t(n) = 4 + n + n² + n + n² + n² 
    # t(n) = 3n² + 2n + 4
    print()

if __name__ == "__main__":
    main()
