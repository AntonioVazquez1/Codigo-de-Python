#Declaramos una variable 
calificacion = input("Intruduce tu calificacion: ")

calificacion = int(calificacion)

# Proguntamos si la calificacion es menos a 700
if calificacion < 700 :
    print("Reprobastes") #Si es menor a 700, muestra esto

elif calificacion > 1000 :
    print("Mientes!!!!! No puedes sacar mas de mil")

else :# Si no se cumple el if anterior , pasa a esta linea 
    print("Felicidades , pasaste la Materia.") # se ejecuta si ninguno de los if se cumple 

# Verificador de mayoria de edad

edad= input("Introduce tu edad")
edad = int(edad)

if edad >= 18 and edad <= 100 : 
    print("Bienvenido al Grupo")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar ")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo ")
else :
    print("No puedes llevarte esos cigarros")