def main():

    def atv1():
        nome = ""
        data = ""
        email = ""
        aux_nome = 0
        aux_email = 0
        aux_data = 0

        nome = input("Digite o seu nome: \n")
        data = input("Digite a sua data: \n")
        email = input("Digite o seu email: \n")

        if data[2] != "/" or data[5] != "/":
            aux_data += 1

        if data[0] == "3" and data[3] == "0"  and data[4] == "2":
            aux_data +=1

        if data[0] == "4":
            aux_data +=1
        for i in range(len(email)):
            if email[i] == "@" and aux_email < 1:
                aux_email += 1
            
            if aux_email == 1 and email[i] == ".":
                aux_email += 1
        for i in range(len(nome)):
            if not nome[i].isalnum:
                aux_nome +=1
        
        if aux_data > 0:
            print("Erro na data")
        elif aux_email != 1:
            print("Erro no email")
        elif aux_nome > 0:
            print("Erro no nome")
        else:
            print("Deu certo")
        
    atv1()

main()