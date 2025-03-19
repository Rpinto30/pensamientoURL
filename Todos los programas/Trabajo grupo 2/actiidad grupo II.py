def comentario():
    c = str(input())
    p = ["herman","idiota","mamahuevo", "gil", "pimpollo", "no te voy a invitar a mi cumpleaños", "si no baila no hay pastel"]

    c = c.lower()
    c = c.replace(",","")
    c = c.replace(".","")
    c = c.replace("#","")

    if p[0] in c: c = c.replace(p[0], "*"*len(p[0]))
    if p[1] in c: c = c.replace(p[1], "*"*len(p[1]))
    if p[2] in c: c = c.replace(p[2], "*"*len(p[2]))
    if p[3] in c: c = c.replace(p[3], "*"*len(p[3]))
    if p[4] in c: c = c.replace(p[4], "*"*len(p[4]))
    if p[5] in c: c = c.replace(p[5], "*"*len(p[5]))
    if p[6] in c: c = c.replace(p[6], "*"*len(p[6]))

    print(c)
    

def noticias():
    noticias = ["URGENTE: Descubren fórmula secreta para la inmortalidad. No quieren que lo sepas!","Estudio revela que el café cura el cáncer. NO TE LO PIERDAS.", "NASA confirma vida en Marte. SECRETO revelado al mundo.", "Gobierno aprueba ley de educación gratuita en todo el país."]
    p = ["URGENTE", "NO TE LO PIERDAS", "NASA", "SEGURO"]
    a = 0

    if  p[0] in noticias[0] or p[1]  in noticias[0] or p[2] in noticias[0] or p[3] in noticias[0]: 
        a += 1
        print("Noticia 1 posiblemente falsa")
    if p[0]  in noticias[1] or p[1]  in noticias[1] or p[2] in noticias[1] or p[3] in noticias[1]: 
        a += 1
        print("Noticia 2 posiblemente falsa")
    if p[0]  in noticias[2] or p[1]  in noticias[2] or p[2] in noticias[2] or p[3] in noticias[2]: 
        a += 1
        print("Noticia 3 posiblemente falsa")
    if p[0]  in noticias[3] or p[1]  in noticias[3] or p[2] in noticias[3] or p[3] in noticias[3]: 
        a += 1
        print("Noticia 4 posiblemente falsa")
        
    print("Cantidad de noticias falsas:" + str(a))
    print("-------------------------------------------")
    print(noticias[0].split()[0] + noticias[0].split()[1] + noticias[0].split()[2])
    print(noticias[1].split()[0] + noticias[1].split()[1] + noticias[1].split()[2])
    print(noticias[2].split()[0] + noticias[2].split()[1] + noticias[2].split()[2])
    print(noticias[3].split()[0] + noticias[3].split()[1] + noticias[3].split()[2])

    if p[0] in noticias[0] or p[0] in noticias[1] or p[0] in noticias[2] or p[0] in noticias[3]: 
        noticias[0].replace(p[0].upper(), p[1].lower())
    if p[1] in noticias[0] or p[1] in noticias[1] or p[1] in noticias[2] or p[1] in noticias[3]: 
        noticias[0].replace(p[0].upper(), p[1].lower())
    if p[2] in noticias[0] or p[2] in noticias[1] or p[2] in noticias[2] or p[2] in noticias[3]: 
        noticias[0].replace(p[0].upper(), p[1].lower())
    if p[3] in noticias[0] or p[3] in noticias[1] or p[3] in noticias[2] or p[3] in noticias[3]:
        noticias[0].replace(p[0].upper(), p[1].lower())
    
    print("-------------------------------------------")
    print(noticias[0])
    print(noticias[1])
    print(noticias[2])
    print(noticias[3])
comentarios_salud = [ "Me siento muy ansioso últimamente, no sé qué hacer.", "Hacer ejercicio me ayudó mucho con la depresión.", "Creo que necesito ayuda profesional para controlar mi estrés.", "Estoy durmiendo mejor y eso ha reducido mi ansiedad." ]
noticias()
