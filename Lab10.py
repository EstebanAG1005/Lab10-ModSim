import random
from PIL import Image, ImageDraw


players = [
    ("LeBron James", random.randint(90, 99), random.randint(150, 200), "SF"),
    ("Kevin Durant", random.randint(88, 97), random.randint(120, 180), "SF"),
    ("Stephen Curry", random.randint(92, 99), random.randint(140, 190), "PG"),
    ("Giannis Antetokounmpo", random.randint(90, 98), random.randint(150, 200), "PF"),
    ("James Harden", random.randint(88, 97), random.randint(130, 190), "SG"),
    ("Kawhi Leonard", random.randint(88, 96), random.randint(130, 180), "SF"),
    ("Anthony Davis", random.randint(90, 98), random.randint(140, 200), "PF"),
    ("Luka Dončić", random.randint(89, 97), random.randint(140, 190), "PG"),
    ("Joel Embiid", random.randint(90, 98), random.randint(150, 200), "C"),
    ("Paul George", random.randint(88, 96), random.randint(120, 180), "SG"),
    ("Damian Lillard", random.randint(88, 95), random.randint(120, 180), "PG"),
    ("Jayson Tatum", random.randint(87, 94), random.randint(110, 170), "SF"),
    ("Donovan Mitchell", random.randint(87, 94), random.randint(110, 170), "SG"),
    ("Devin Booker", random.randint(87, 94), random.randint(110, 170), "SG"),
    ("Karl-Anthony Towns", random.randint(88, 95), random.randint(130, 190), "C"),
    ("Zion Williamson", random.randint(88, 95), random.randint(130, 190), "PF"),
    ("Ben Simmons", random.randint(87, 94), random.randint(110, 170), "PG"),
    ("Jaylen Brown", random.randint(87, 94), random.randint(110, 170), "SG"),
    ("De'Aaron Fox", random.randint(87, 94), random.randint(110, 170), "PG"),
    ("Ja Morant", random.randint(87, 94), random.randint(110, 170), "PG"),
    ("Deandre Ayton", random.randint(88, 95), random.randint(130, 190), "C"),
    ("Jaren Jackson Jr.", random.randint(87, 94), random.randint(110, 170), "PF"),
    ("Collin Sexton", random.randint(87, 94), random.randint(100, 160), "PG"),
    ("Shai Gilgeous-Alexander", random.randint(87, 94), random.randint(100, 160), "SG"),
    ("Michael Porter Jr.", random.randint(87, 94), random.randint(120, 180), "SF"),
    ("D'Angelo Russell", random.randint(87, 94), random.randint(110, 170), "PG"),
    ("John Collins", random.randint(87, 94), random.randint(100, 160), "PF"),
    ("Brandon Ingram", random.randint(88, 95), random.randint(130, 190), "SF"),
    ("Mikal Bridges", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Lonzo Ball", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("Jonas Valančiūnas", random.randint(86, 93), random.randint(90, 150), "C"),
    ("Malcolm Brogdon", random.randint(86, 93), random.randint(90, 150), "PG"),
    ("Gordon Hayward", random.randint(86, 93), random.randint(90, 150), "SF"),
    ("Bam Adebayo", random.randint(88, 95), random.randint(130, 190), "C"),
    ("Chris Paul", random.randint(87, 94), random.randint(100, 160), "PG"),
    ("Rudy Gobert", random.randint(88, 95), random.randint(130, 190), "C"),
    ("Tobias Harris", random.randint(86, 93), random.randint(100, 160), "SF"),
    ("Kemba Walker", random.randint(86, 93), random.randint(90, 150), "PG"),
    ("Russell Westbrook", random.randint(87, 94), random.randint(110, 170), "PG"),
    ("Kristaps Porziņģis", random.randint(88, 95), random.randint(120, 180), "PF"),
    ("DeMar DeRozan", random.randint(87, 94), random.randint(110, 170), "SG"),
    ("Zach LaVine", random.randint(87, 94), random.randint(100, 160), "SG"),
    ("Nikola Vucevic", random.randint(88, 95), random.randint(120, 180), "C"),
    ("CJ McCollum", random.randint(87, 94), random.randint(100, 160), "SG"),
    ("Kyle Lowry", random.randint(86, 93), random.randint(90, 150), "PG"),
    ("Ja Morant", random.randint(87, 94), random.randint(110, 170), "PG"),
    ("Chris Middleton", random.randint(86, 93), random.randint(90, 150), "SF"),
    ("Devonte' Graham", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("Jaren Jackson Jr.", random.randint(87, 94), random.randint(100, 160), "PF"),
    ("Jarrett Allen", random.randint(85, 92), random.randint(80, 140), "C"),
    ("Darius Garland", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("De'Andre Hunter", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Rui Hachimura", random.randint(85, 92), random.randint(80, 140), "PF"),
    ("LaMelo Ball", random.randint(88, 95), random.randint(120, 180), "PG"),
    ("Anthony Edwards", random.randint(87, 94), random.randint(110, 170), "SG"),
    ("Cole Anthony", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("James Wiseman", random.randint(87, 94), random.randint(100, 160), "C"),
    ("Obi Toppin", random.randint(85, 92), random.randint(80, 140), "PF"),
    ("Killian Hayes", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("Isaac Okoro", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Onyeka Okongwu", random.randint(85, 92), random.randint(80, 140), "C"),
    ("Deni Avdija", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Tyrese Haliburton", random.randint(86, 93), random.randint(90, 150), "PG"),
    ("Patrick Williams", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Devin Vassell", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Precious Achiuwa", random.randint(85, 92), random.randint(80, 140), "PF"),
    ("Isaiah Stewart", random.randint(85, 92), random.randint(80, 140), "C"),
    ("Saddiq Bey", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Tyrese Maxey", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Aaron Nesmith", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Immanuel Quickley", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("Desmond Bane", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Payton Pritchard", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("Zeke Nnaji", random.randint(85, 92), random.randint(80, 140), "PF"),
    ("Leandro Bolmaro", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Xavier Tillman", random.randint(85, 92), random.randint(80, 140), "C"),
    ("Robert Woodard II", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Jahmi'us Ramsey", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Vernon Carey Jr.", random.randint(85, 92), random.randint(80, 140), "C"),
    ("Nick Richards", random.randint(85, 92), random.randint(80, 140), "C"),
    ("Elijah Hughes", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Cassius Winston", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("Tre Jones", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("Nico Mannion", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("Isaiah Joe", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Jordan Nwora", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Jalen Smith", random.randint(85, 92), random.randint(80, 140), "PF"),
    ("Jalen Harris", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Luka Šamanić", random.randint(85, 92), random.randint(80, 140), "PF"),
    ("Quinndary Weatherspoon", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Jarrell Brantley", random.randint(85, 92), random.randint(80, 140), "PF"),
    ("Miye Oni", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Dewan Hernandez", random.randint(85, 92), random.randint(80, 140), "PF"),
    ("Justin James", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Kyle Guy", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Marial Shayok", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Admiral Schofield", random.randint(85, 92), random.randint(80, 140), "SF"),
    ("Jordan Bone", random.randint(85, 92), random.randint(80, 140), "PG"),
    ("Talen Horton-Tucker", random.randint(85, 92), random.randint(80, 140), "SG"),
    ("Kostas Antetokounmpo", random.randint(85, 92), random.randint(80, 140), "PF"),
]

BUDGET = 2000  # presupuesto máximo


def fitness(team):
    """Calcula la aptitud de un equipo"""
    score = sum([player[1] for player in team])
    cost = sum([player[2] for player in team])
    if cost > BUDGET:
        return 0  # penalización si supera el presupuesto
    return score


def initialize_population(num_teams):
    """Inicializa una población de equipos aleatorios con todas las posiciones"""
    teams = []
    for _ in range(num_teams):
        team = []
        for position in ["PG", "SG", "SF", "PF", "C"]:
            players_at_position = [p for p in players if p[3] == position]
            team.append(random.choice(players_at_position))
        teams.append(team)
    return teams


def select_parents_tournament(population, k=3):
    """Selección por torneo"""
    selected = random.sample(population, k)
    return max(selected, key=fitness)


def crossover(parent1, parent2):
    """Crossover de dos puntos"""
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    offspring = parent1[start:end]
    for player in parent2:
        if player not in offspring:
            offspring.append(player)
    return offspring[:size]


def mutate(team):
    """Reemplaza un jugador por otro aleatorio"""
    idx = random.randint(0, len(team) - 1)
    new_player = random.choice(players)
    while new_player in team:
        new_player = random.choice(players)
    team[idx] = new_player
    return team


def genetic_algorithm_NBA(iterations=1000, population_size=100):
    population = initialize_population(population_size)
    for _ in range(iterations):
        new_population = []
        for _ in range(population_size):
            parent1 = select_parents_tournament(population)
            parent2 = select_parents_tournament(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    best_solution = max(population, key=fitness)
    return best_solution


def visualize_team(team):
    # Carga la imagen de la cancha
    court_image = Image.open("cancha.jpg")  # Reemplaza "cancha.jpg" con la ruta de tu propia imagen

    # Crea un objeto para dibujar en la imagen
    draw = ImageDraw.Draw(court_image)

    positions = {
        1: (130, 70),  # Ajusta las coordenadas según tu imagen
        2: (50, 100),
        3: (200, 100),
        4: (50, 200),
        5: (200, 200),
    }

    for i, player in enumerate(team):
        position = i+1
        x, y = positions.get(position, (0, 0))  # Default pos if position is missing
        name = player[0]
        name = (name[:15] + "..") if len(name) > 15 else name

        # Dibuja el jugador en la imagen
        draw.text((x, y), name, fill=(0, 0, 0))  # Ajusta el color y la posición

    # Muestra la imagen con los jugadores
    court_image.show()


# Probamos el algoritmo y visualizamos el equipo resultante:
best_team = genetic_algorithm_NBA()

# Ordena el best_team por las posiciones: PG, SG, SF, PF y C
best_team_sorted = sorted(best_team, key=lambda x: (("PG", "SG", "SF", "PF", "C").index(x[3]), -x[1]))

print("\nMejor equipo encontrado:")
for player in best_team_sorted:
    print(player)
visualize_team(best_team_sorted)
