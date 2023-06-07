import random

def best_first_search(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira = []
    nosVisitados = []
    fronteira.append(inicio)

    bestFirstPath = {}
    bestFirstCost = {} 

    # Define o custo inicial do vértice inicial como 0
    bestFirstCost[inicio] = 0

    while fronteira != []:
        # Ordena a fronteira com base no custo mínimo
        fronteira.sort(key=lambda v: bestFirstCost[v])
        vertice = fronteira.pop(0)
        nosVisitados.append(vertice)

        if vertice == labirinto._goal:
            print("objetivo encontrado")
            break

        movimentos = ["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[vertice][d] == True:
                if d == 'E':
                    vizinho = (vertice[0], vertice[1] + 1)
                if d == 'W':
                    vizinho = (vertice[0], vertice[1] - 1)
                if d == 'N':
                    vizinho = (vertice[0] - 1, vertice[1])
                if d == 'S':
                    vizinho = (vertice[0] + 1, vertice[1])

                # Calcula o custo mínimo para o vizinho
                novoCusto = bestFirstCost[vertice] + 1

                if vizinho not in nosVisitados and vizinho not in fronteira:
                    # Adiciona o vizinho à fronteira e ao dicionário de caminhos e custos
                    fronteira.append(vizinho)
                    bestFirstPath[vizinho] = vertice
                    bestFirstCost[vizinho] = novoCusto
                elif vizinho in fronteira and novoCusto < bestFirstCost[vizinho]:
                    # Atualiza o custo mínimo e o caminho se um custo menor for encontrado
                    bestFirstPath[vizinho] = vertice
                    bestFirstCost[vizinho] = novoCusto

    fwdPath = {}
    cell = labirinto._goal
    while cell != inicio:
        fwdPath[bestFirstPath[cell]] = cell
        cell = bestFirstPath[cell]
    return fwdPath