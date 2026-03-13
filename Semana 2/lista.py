def main():
    # Questão 1:
    # Tuplas não podem ser alteradas após a sua criação, ao contrário das listas, que podem ser mudadas a qualquer momento

    # Questão 2:
    # A lista se transformarar em um conjunto, dessa forma ele eliminará todos os elementos repetidos, os elementos entram em desordem
    #e os elementos não poderão ser alterados.

    #Questão 3
    # numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(f"Questão 3 Letra A: {numeros[0:3]}")
    # print(f"Questão 3 Letra B: {numeros[5:9]}")
    # A) Eu pegaria a lista aplicaria o seguinte comando numeros[0:3] que pegaria todo os valores começando da posição 0 e indo até a 3 (excluindo ela)
    # A) Eu pegaria a lista aplicaria o seguinte comando numeros[5:9] que pegaria todo os valores começando da posição 5 e indo até a 9 (excluindo ela)

    # Questão 4
    # texto = "banana"
    # aux = []
    # dicio = {
    #     "b": 0,
    #     "a": 0,
    #     "n": 0
    # }
    # for i in texto: 
    #     if i not in aux:
    #         for n in texto:
    #             if i == n:
    #                 dicio[i] += 1
    #             aux.append(i)
    # print(dicio)
    # Para um sistema genérico que criei uma variável auxiliar (aux), a variável com o texto e a variável com o dicionário. Então criei um for que coletaria
    # a letra do texto (i), então em um if verificava se i estava dentro de aux, se não ele entraria em um segundo for (n) que percorreria o texto de novo
    # e entraria em um segundo if que verificaria se i é igual a n, se sim adicionaria mais 1 na contagem dentro de dicio na letra que i está guardando
    # (dicio[i] +=1). Após o código guardaria a letra que estava em i dentro de aux. Dessa forma quando ele retornar para o for inicial ele não contara as 
    # letras 2 vezes.

    # Questão 5
    # alun1 = {
    #     "nome" : "Thomas",
    #     "notas" : [8,9,3,1]
    # }
    # alun2 = {
    #     "nome" : "Pedro Lucas",
    #     "notas" : [2,4,6,1]
    # }
    # alun3 = {
    #     "nome" : "Pedro Henrique",
    #     "notas" : [8,9,3,1]
    # }
    # listAlun = [alun1,alun2,alun3]

    # print (listAlun[0]["notas"][1])
    # Primeiro eu acessaria a primeira posição da lista com o alunos (listAlun[0]), depois acessaria as notas do aluno 1 (listAlun[0]["notas"]) e por
    # fim iria acessar o segundo termo da lista de notas (listAlun[0]["notas"][1])

    # Questão 6
    # nomes = ['ana', 'bia', 'caio']
    # dicioNomes = {}
    # for i in range(len(nomes)):
    #     dicioNomes.update({nomes[i]: len(nomes[i])})
    # print(dicioNomes)
    # em um for (i), que se repetia o numero de vezes igual a quantidade de valores na lista de nome (3), eu fazia dicioNomes.update({nomes[i]: len(nomes[i])})
    # onde em toda repetição do for ele vai adicionar o nome (nomes[i]) como chave e a quantidade de letras do nome (len(nomes[i]))

    # Questão 7


    # Questão 8
    # listaCompras = []
    # listaCompras.append("Celular")
    # listaCompras.append("Fone")
    # listaCompras.append("Capa")
    # print(f"Lista de compras: {listaCompras}")
    # listaCompras.remove("Capa")
    # print(f"Lista de compras2: {listaCompras}")

    # Questão 9
    # frutas =  {"maçã": 10, "banana": 15}
    # frutas["banana"] = 20
    # frutas["uva"] = 5
    # frutas["caju"] = 0
    # for i in frutas:
    #     if frutas[i] != 0:
    #         print(f"Fruta: {i} | Quantidade {frutas[i]}")

    # Questão 10
    # def imprimeLista(lista):
    #     for i in lista:
    #         print(i)

    # liss =[2,4,6,78,8,9,9]
    # imprimeLista(liss)
    print("")
    

if __name__ == "__main__":
    main()