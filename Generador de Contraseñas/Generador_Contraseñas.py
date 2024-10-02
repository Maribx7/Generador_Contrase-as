import random
import string

# Función para medir la seguridad de la contraseña
def evaluar_seguridad(password):
    long = len(password)
    mayusculas = sum(1 for c in password if c.isupper())
    minusculas = sum(1 for c in password if c.islower())
    numeros = sum(1 for c in password if c.isdigit())
    simbolos = sum(1 for c in password if c in string.punctuation)

    score = long + mayusculas + minusculas + numeros + simbolos
    if score < 8:
        return "Débil"
    elif 8 <= score < 12:
        return "Moderada"
    else:
        return "Fuerte"

# Generador de contraseña básica
def generar_contraseña(longitud=12, incluir_simbolos=True, incluir_numeros=True):
    caracteres = string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

# Generador de contraseña temática
def generar_contraseña_con_tema(tema="espacio"):
    palabras = {
        "espacio": ["estrellas", "galaxia", "luna", "orbitar", "cometa"],
        "naturaleza": ["bosque", "oceano", "montaña", "río", "selva"],
    }
    
    contraseña = random.choice(palabras.get(tema, []))
    contraseña += random.choice(string.digits)
    contraseña += random.choice(string.punctuation)
    
    return contraseña

# Generador desde frase
def generar_contraseña_desde_frase(frase):
    frase = frase.replace(" ", "").lower()
    frase_segura = frase.replace('a', '@').replace('e', '3').replace('i', '1').replace('o', '0')
    frase_segura += str(random.randint(10, 99)) + random.choice(string.punctuation)
    return frase_segura
