a1= int(input("Digite o ano de seu nascimento :"))
a2= (a1-2020)
a3= (18-(a2))
a4= (a3 / a3)
a5= ((-2020)+a2)
a6= (-1*a5)
#use (-1*) because with this we can transform a5(negative) in positive
if a1 - 2020 == -18:
    print("você deve se alistar este ano")
elif a1-2020 > -18:
    print(f"Você ainda vai se alistar. especificamente em {a6}")
elif a1-2020 < -18:
    print(f"já passou seu alistamento, você devia ter se alistado em 2020 você está {a4} anos atrasado")