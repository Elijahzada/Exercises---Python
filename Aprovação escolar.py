a1= float(input("Insira a nota da sua prova : "))
a2= float(input("insira a nota da segunda prova :"))
a3= (a1 + a2) /2
if a3 > 7.0:
    print(f"Parabéns você foi aprovado,sua nota foi {a3}")
elif a3 < 5.0:
    print("você reprovou parabéns")
elif a3  >= 5.5 and a3 <= 7.0:
    #Here i use >= because i dont know how use range lol :)
    print("você está de recuperação")