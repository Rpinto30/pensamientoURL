comentarios = ["Eres un idiota, no sabes nada.", "Qué gran aporte, muchas gracias.", "Tu opinión es basura, nadie te pidió hablar.", "Increíble descubrimiento, gracias por compartir."]
p_prohibidas = ["idiota", "basura"]
n = int(input("Selecciona un comentario con un número del 1 al " + str(len(comentarios)) + ": "))

c = comentarios[n-1]
c = c.lower()
c = c.replace(",", "").replace(".", "")

if p_prohibidas[0] in comentarios[n-1]:
    c = c.replace(p_prohibidas[0], "*"*len(p_prohibidas[0]))
elif p_prohibidas[1] in comentarios[n-1]:
    c = c.replace(p_prohibidas[1], "*"*len(p_prohibidas[1]))

print(c)


