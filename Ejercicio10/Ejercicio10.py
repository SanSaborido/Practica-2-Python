# Importacion de las funciones posteriormente solicitadas.
import Functions

# Datos.
names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]

# Ordenamiento de los datos en una sola estructura.
data = Functions.structure_creator(names, goals, goals_avoided, assists)
print("Tabla de jugadores con todos sus datos:")
print(data)
print("-------------")

# Calculo del goleador o goleadora del equipo.
goal_scorer = Functions.best_scorer(data)
print(f"Nombre del goleador o goleadora:", goal_scorer[0]," y sus goles:",goal_scorer[1])
print("-------------")

# Calculo del jugador o jugadora mas influyente.
print(f"El jugador o jugadora mas influyente es: ", (Functions.best_player(data)))
print("-------------")

# Calculo de promedio de goles del equipo.
team_goals = lambda: sum(goals)/25
print(f"El promedio de goles del equipo es: ", team_goals())
print("-------------")

# Calculo de promedio de goles del goleador.
player_average = lambda: goal_scorer[1]/25
print(f"El promedio de goles del goleador es: ", player_average())
