#VARIABLES, FUNCION PRINT


'''
NO INICIAR CON:
-CARACTERES ESPECIALES
-NUMEROS
-MAYUSCULAS
'''
var_estatura = 1.8
var_peso = 80
var_nombre = "Juanito Perez"
var_imc = var_peso/(var_estatura*var_estatura)

print(str(var_nombre), "mide: " + str(var_estatura) + "m", "pesa: " + str(var_peso) + "kg")
print("El IMC de" + str(var_nombre) + "es de: " + str(var_imc))