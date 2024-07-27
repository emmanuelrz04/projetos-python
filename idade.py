idade = int(input("que ano você nasceu? "))
ano = int(input("que ano estamos? "))
nascimento = ano - idade
corr = input("está ou já passou do mês do seu aniversário? ")
if corr == "nao" or corr == "Não":
    print(f"você tem {nascimento - 1} anos de idade")
elif corr == "sim" or corr == "Sim":
    print (f"você tem {nascimento} anos de idade")
