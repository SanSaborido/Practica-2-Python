# Funcion encargada de generar un diccionario con todos los datos recibidos.

def structure_creator (names, goals, goals_avoided, assists):
    stats = zip(names.split(","), goals, goals_avoided, assists)    
    new_structure = {}    
    for name, goal, goal_avoided, assist in stats:
        new_structure[name] = {"Goles:": goal, "Goles evitados:": goal_avoided, 
                               "Asistencias:": assist}
    return new_structure


