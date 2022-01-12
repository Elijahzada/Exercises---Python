import math
A1=int(input("Qual o valor da casa que você deseja? R$ "))
A2= int(input("Qual seu salário?"))
A3= int(input("Em quantos anos vai pagar?"))
A4= int(12*A3)
A5= (float( A1 / A4))
A6= (int(0.3 * A2))
A7= (A4*A5)
if A5 < A6:
    print(f"emprestimo concedido, você vai pagar {A4} parcelas, de {math.trunc(A5)} Reais,valor total de {A7} reais ")
else:
    print("Limite recusado")