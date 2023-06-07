import random
import math

def heuristic(a, b):
    """
    Função heurística para estimar a distância entre dois pontos.
    Neste caso, é utilizada a distância Euclidiana.
    """
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

def aStar(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    goal = labirinto._goal

    open_set = set()
    closed_set = set()
    came_from = {}

    g_score = {inicio: 0}
    f_score = {inicio: heuristic(inicio, goal)}

    open_set.add(inicio)

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])

        if current == goal:
            print("Objetivo encontrado")
            break

        open_set.remove(current)
        closed_set.add(current)

        movimentos = ["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[current][d] == True:
                if d == 'E':
                    vizinho = (current[0], current[1] + 1)
                if d == 'W':
                    vizinho = (current[0], current[1] - 1)
                if d == 'N':
                    vizinho = (current[0] - 1, current[1])
                if d == 'S':
                    vizinho = (current[0] + 1, current[1])

                if vizinho in closed_set:
                    continue

                tentative_g_score = g_score[current] + 1

                if vizinho not in open_set:
                    open_set.add(vizinho)
                elif tentative_g_score >= g_score[vizinho]:
                    continue

                came_from[vizinho] = current
                g_score[vizinho] = tentative_g_score
                f_score[vizinho] = g_score[vizinho] + heuristic(vizinho, goal)

    fwdPath = {}
    cell = goal
    while cell != inicio:
        fwdPath[came_from[cell]] = cell
        cell = came_from[cell]
    return fwdPath