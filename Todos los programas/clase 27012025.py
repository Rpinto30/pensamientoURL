print("Está soleado? (Solo si o no)")
soleado = "no"
while True:
    soleado = input()
    if str(soleado).lower() != "no" or str(soleado).lower() != "si": break

soleado = True
lloviendo = False
puntual = False

if puntual and soleado: print("Toma bus")
elif puntual == False and lloviendo: print("Toma taxi")
else: print("Que coma verga")