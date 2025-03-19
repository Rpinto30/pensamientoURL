n = int(input("Ingresa la cantidad de dinero facturado: \nQ"))
timbre_50 = n//10000
timbre_10 = n%10000//2000
timbre_5 = n%10000%2000//1000

if n%10000%2000%1000 == 0:
      timbre_1 = (n%10000%2000%1000//200)
else:
      timbre_1 = (n%10000%2000%1000//200) +1

print("--------------Cantidad de timbres--------------")
print("Timbres de Q50: " + str(timbre_50) + "\n" +
      "Timbres de Q10: " + str(timbre_10) + "\n" +
      "Timbres de Q5: "  + str(timbre_5) + "\n" +
      "Timbres de Q1: "  + str(timbre_1))

