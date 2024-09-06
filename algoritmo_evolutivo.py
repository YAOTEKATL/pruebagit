import random

# Parámetros del algoritmo
num_equipos = 10
num_miembros = 10
prob_mutacion = 0.1

def generar_equipo():
    return [(random.randint(0, 1), random.randint(0, 1)) for _ in range(num_miembros)]

def inicializar_poblacion():
    return [generar_equipo() for _ in range(num_equipos)]

def contar_pares_11(equipo):
    return sum(1 for miembro in equipo if miembro == (1, 1))

def evaluar_poblacion(poblacion):
    return [contar_pares_11(equipo) for equipo in poblacion]

def seleccion_torneo(poblacion, aptitudes):
    seleccionados = []
    indices = list(range(len(poblacion)))
    random.shuffle(indices)
    for i in range(len(poblacion) // 2):
        idx1, idx2 = indices[2 * i], indices[2 * i + 1]
        if aptitudes[idx1] > aptitudes[idx2]:
            seleccionados.append(poblacion[idx1])
        else:
            seleccionados.append(poblacion[idx2])
    return seleccionados

def cruzamiento(equipo1, equipo2):
    punto_cruzamiento = random.randint(1, num_miembros - 1)
    hijo1 = equipo1[:punto_cruzamiento] + equipo2[punto_cruzamiento:]
    hijo2 = equipo2[:punto_cruzamiento] + equipo1[punto_cruzamiento:]
    return hijo1, hijo2

def mutacion(equipo):
    for i in range(num_miembros):
        if random.random() < prob_mutacion:
            equipo[i] = (random.randint(0, 1), random.randint(0, 1))
    return equipo

def evolucionar(poblacion):
    aptitudes = evaluar_poblacion(poblacion)
    seleccionados = seleccion_torneo(poblacion, aptitudes)
    
    nuevos_equipos = []
    while len(nuevos_equipos) < num_equipos:
        equipo1, equipo2 = random.sample(seleccionados, 2)
        hijo1, hijo2 = cruzamiento(equipo1, equipo2)
        nuevos_equipos.append(mutacion(hijo1))
        if len(nuevos_equipos) < num_equipos:
            nuevos_equipos.append(mutacion(hijo2))
    
    return nuevos_equipos

def main():
    poblacion = inicializar_poblacion()
    generaciones = 10
    for _ in range(generaciones):
        poblacion = evolucionar(poblacion)
        aptitudes = evaluar_poblacion(poblacion)
        mejor_aptitud = max(aptitudes)
        print(f"Mejor aptitud en esta generación: {mejor_aptitud}")

if __name__ == "__main__":
    main()
