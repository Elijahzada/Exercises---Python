a1=int(input("Digite o ano de seu nascimento:"))
a2= (2021-a1)
if a2 == 19:
    print("Você foi designado para classe sênior")
elif a2 >= 15 and a2 <= 18:
    print("você foi designado para a classe Junior")
elif a2 >= 10 and a2 <= 14:
    print("você foi designado para a classe Infantil")
elif a2 == 9:
    print("você foi designado para a classe Mirim")