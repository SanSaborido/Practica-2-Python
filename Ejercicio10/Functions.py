# Funcion encargada de generar un diccionario con todos los datos recibidos.

def structure_creator (names, goals, goals_avoided, assists):
    stats = zip(names.split(","), goals, goals_avoided, assists)    
    new_structure = {}    
    for name, goal, goal_avoided, assist in stats:
        new_structure[name] = {"Goles:": goal, "Goles evitados:": goal_avoided, 
                               "Asistencias:": assist}
    return new_structure

# Funcion encargada de devolver el nombre y cantidad de goles del goleador.

def best_scorer (new_structure):
    max_name = max(new_structure, key=lambda x: new_structure[x]["Goles:"])
    max_goals = new_structure[max_name]["Goles:"]
    return max_name, max_goals

# Funcion encargada de devolver el nombre del jugador mas influyente.

def best_player (new_structure):
    max_player = max(new_structure, key=lambda x: new_structure[x]["Goles:"]*1.5
                     + new_structure[x]["Goles evitados:"]*1.25
                     + new_structure[x]["Asistencias:"])
    return max_player
    