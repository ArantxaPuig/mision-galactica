#Bienvenida
print("Bienvenid@s a la misión galáctica 🪐\n")

# Variables de la capitana
capitana = 'Arantxa'
energia = 75
escudo_activo = True
print(f"{capitana} {energia} {escudo_activo}\n")

# Verificar tipos
assert isinstance(capitana, str), 'capitana debe ser texto'
assert isinstance(energia, (int, float)), 'energia debe ser número'
assert isinstance(escudo_activo, bool), 'escudo_activo debe ser booleano'
print('✅ Reto 1 OK\n')

# Mensaje estado capitana
estado_escudo = "activo" if escudo_activo else "inactivo"
mensaje = f"La capitana {capitana} tiene {energia} de energía y su escudo está {estado_escudo}."
print(mensaje)
print('✅ Reto 1 OK\n')

# Condicional aterrizaje
energia = 45
escudo = 60

if energia >= 40 and escudo >= 50:
    print("🛬 Aterrizaje autorizado ✅\n")
else:
    print("⛔ Aterrizaje denegado\n")

# Recorrer módulos
modulos = ['motor', 'radar', 'escudos', 'comunicaciones', "panel", "apertura automática"]

for modulo in modulos:
    print(f"🔍 Revisando módulo: {modulo}")
print()

# Función puntos_mision
def puntos_mision(tareas, bonus):
    return tareas * 10 + bonus

print('Puntos:', puntos_mision(6, 12))
assert puntos_mision(2, 5) == 25
print('✅ Reto 4 OK\n')

# Diccionario piloto
pilota = {
    "nombre": "Arantxa",
    "rol": "Capitana",
    "nivel": 5
}

print(f"{pilota['nombre']} tiene el rol de {pilota['rol']}\n")

# Barra de progreso en consola
import time
progreso_final = 75
for progreso in range(progreso_final + 1):
    barra = '█' * (progreso // 2) + '-' * ((100 - progreso) // 2)
    print(f"\rProgreso: |{barra}| {progreso}%", end="")
    time.sleep(0.05)
print("\n")  # salto de línea al final

# Elegir planeta al azar
import random
planetas = ['🪐 Saturno', '🔴 Marte', '🌕 Luna', '🌌 Nebulosa X']
destino = random.choice(planetas)
print(f"🚀 Preparando la nave... ¡Nuestro destino será {destino}!\n")

# Cuenta atrás antes del despegue
print("🚀 Preparando el despegue...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)
print("¡Despegue! 🚀")