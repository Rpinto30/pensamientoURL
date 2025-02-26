consumo = int(input("Ingrese cantidad de consumo:\n" + "Q"))
pagada = int(input("Ingrese cantidad para pagar:\n" + "Q"))

vuelto = pagada-consumo

c_200 = vuelto//200
c_100 = (vuelto%200)//100
c_50 = (vuelto%200)%(100)//50
c_20 = (vuelto%200)%100%50//20
c_10 = (vuelto%200)%100%50%20//10
c_5 = (vuelto%200)%100%50%20%10//5
c_1 = (vuelto%200)%100%50%20%10%5//1

print("--------------Cantidad de vuelto a dar: " + "Q" + str(vuelto) + "--------------")

print(" -Billetes de 200: " + str(c_200) + "\n"
      " -Billetes de 100: " + str(c_100) + "\n"
      " -Billetes de 50: " + str(c_50) + "\n"
      " -Billetes de 20: " + str(c_20) + "\n"
      " -Billetes de 10: " + str(c_10) + "\n"
      " -Billetes de 5: " + str(c_5) + "\n"
      " -Monedas de 1: " + str(c_1))