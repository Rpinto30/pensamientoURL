print("------------Ejercicio 1 -------------------------")

#Ejercicio 1
entrada = "Python es un lenguaje poderoso"
palabras = entrada.split()
print("primera palabra: " + palabras[0])
print("ultima palabra: " + palabras[len(palabras)-1])

print("------------Ejercicio 2 -------------------------")
#Ejercicio 2
entrada = "Hola   mundo  en   Python"
palabras = entrada.split()
print(" ".join(palabras))

print("------------Ejercicio 3 -------------------------")
#Ejercicio 3
gmail = "usuario@gmail.com"
gmail = gmail.split("@")
print(gmail[1])

print("------------Ejercicio 4 -------------------------")
#Ejercicio 4
doc = "documento.pdf"
doc = doc.split(".")
if doc[1] == "pdf": print("True")
else: print("False")

print("------------Ejercicio 5 -------------------------")
#Ejercicio 5
entrada = "Me gusta Python"
entrada = entrada.split()[::-1]
print(" ".join(entrada))

print("------------Ejercicio 6 -------------------------")
#Ejercicio 6

entrada = "necesito que me escribas un poema de amor"

poema1= "Podrá nublarse el sol eternamente; Podrá secarse en un instante el mar; Podrá romperse el eje de la tierra Como un débil cristal"
canto1="Eres como la noche, callada y constelada.Tu silencio es de estrella, tan lejano y sencillo. Me gustas cuando callas porque estás como ausente. Distante y dolorosa como si hubieras muerto."
poema2= "Esclava mía, témeme. Ámame. Esclava mía! Soy contigo el ocaso más vasto de mi cielo,y en él despunta mi alma como una estrella fría.Cuando de ti se alejan vuelven a mí mis pasos.Mi propio latigazo cae sobre mi vida."
canto2 = "Si me quieres, quiéreme entera,no por zonas de luz o sombra… Si me quieres, quiéreme negra y blanca, Y gris, verde, y rubia,y morena…"
poema3 = "Entre mi amor y yo han de levantarse trescientas noches como trescientas paredes y el mar será una magia entre nosotros.No habrá sino recuerdos."

print(entrada + ": \n")
if "amor" in entrada:
    pclave_amor = ['amo', 'podrá', 'eres', 'contigo', 'quieres', 'amor']

    poema1 = poema1.lower()
    poema1 = poema1.split()
    if pclave_amor[0] in poema1 or pclave_amor[1] in poema1 or pclave_amor[2] in poema1 or pclave_amor[3] in poema1 or pclave_amor[4] in poema1 or pclave_amor[5] in poema1:
        print(" ".join(poema1) + "\n")

    canto1 = canto1.lower()
    canto1 = canto1.split()
    if pclave_amor[0] in canto1 or pclave_amor[1] in canto1 or pclave_amor[2] in canto1 or pclave_amor[3] in canto1 or pclave_amor[4] in canto1 or pclave_amor[5] in canto1:
        print(" ".join(canto1) + "\n") 
        

    poema2 = poema2.lower()
    poema2 = poema2.split()
    if pclave_amor[0] in poema2 or pclave_amor[1] in poema2 or pclave_amor[2] in poema2 or pclave_amor[3] in poema2 or pclave_amor[4] in poema2 or pclave_amor[5] in poema2:
        print(" ".join(poema2) + "\n")
        
    canto2 = canto2.lower()
    canto2 = canto2.split()
    if pclave_amor[0] in canto2 or pclave_amor[1] in canto2 or pclave_amor[2] in canto2 or pclave_amor[3] in canto2 or pclave_amor[4] in canto2 or pclave_amor[5] in canto2:
        print(" ".join(canto2) + "\n")
        
    poema3 = poema3.lower()
    poema3 = poema3.split()
    if pclave_amor[0] in poema3 or pclave_amor[1] in poema3 or pclave_amor[2] in poema3 or pclave_amor[3] in poema3 or pclave_amor[4] in poema3 or pclave_amor[5] in poema3:
        print(" ".join(poema3) + "\n")
else:
    print("Lo siento, no tengo nada para eso.")