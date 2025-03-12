n = [ "URGENTE Descubren fórmula secreta para la inmortalidad. No quieren que lo sepas!", "Estudio revela que el café cura el cáncer. NO TE LO PIERDAS.", "NASA confirma vida en Marte. SECRETO revelado al mundo.", "Gobierno aprueba ley de educación gratuita en todo el país."]
p = ["URGENTE", "NO TE LO PIERDA", "SECRETO"]
a = 0

if  p[0] in n[0] or p[1]  in n[0] or p[2] in n[0]: 
    a += 1
    print("Noticia 1 posiblemente falsa")
if p[0]  in n[1] or p[1]  in n[1] or p[2] in n[1]: 
    a += 1
    print("Noticia 2 posiblemente falsa")
if p[0]  in n[2] or p[1]  in n[2] or p[2] in n[2]: 
    a += 1
    print("Noticia 3 posiblemente falsa")
if p[0]  in n[3] or p[1]  in n[3] or p[2] in n[3]: 
    a += 1
    print("Noticia 4 posiblemente falsa")
    
print("Cantidad de noticias falsas:" + str(a))
print("-------------------------------------------")
print(n[0].split()[0] + n[0].split()[1] + n[0].split()[2])
print(n[1].split()[0] + n[1].split()[1] + n[1].split()[2])
print(n[2].split()[0] + n[2].split()[1] + n[2].split()[2])
print(n[3].split()[0] + n[3].split()[1] + n[3].split()[2])
print("-------------------------------------------")

print(n[0].lower())
print(n[1].lower())
print(n[2].lower())
