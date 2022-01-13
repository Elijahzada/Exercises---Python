a1= int(input("Qual valor você deseja ?"))
a2= int(input("Base de conversão para :\n 1- para Binario\n 2- para Octal\n 3- Hexadecimal\n"))
if a2 == 1:
     a3 = bin(int(f"{a1}"))
     print(f"O valor binario é {a3}")
elif a2 == 2:
     a4 = oct(int(f"{a1}"))
     print(f"O valor binario é {a4}")
elif a2 == 3:
     a5 = hex(int(f"{a1}"))
     print(f"O valor binario é {a5}")
     #This is a calculator of Hex,oct,and bin.


