from pyamaze import maze, agent
from random import randint
from bfs import *
from dfs import *
from aStar import *
from bfsCost import *
from bfsBestFirst import *

def execucaoMaze(tamanho=10, possibilidadeCaminhos=100, algoritmo=""):
    
    goalX, goalY = randint(1,tamanho), 1
    
    m=maze(tamanho,tamanho)
    m.CreateMaze(goalX, goalY, loopPercent=possibilidadeCaminhos)
    
    # Inclusao do agente no ambiente
    a=agent(m,footprints=True, shape="arrow")
    b=agent(m,footprints=True, color='red', filled=True)

    #m.run()
    
    if algoritmo=="bfs":
        print("Executando a busca em largura")
        path1=bfs(m)
        path2=bfs(m)    
    elif algoritmo=="dfs":
        print("Executando a busca em profundidade")
        path1=dfs(m)
        path2=dfs(m)
    elif algoritmo=="aStar":
        print("Executando a busca em A*")
        path1=aStar(m)
        path2=aStar(m)
    elif algoritmo=="bfsCost":
        print("Executando a busca bfs com custo mínimo")
        path1=bfsCost(m)
        path2=bfsCost(m)
    elif algoritmo=="bestFirst":
        print("Executando a busca bfs com Best First")
        path1=best_first_search(m)
        path2=best_first_search(m)
    else:
        path = m.path
    m.tracePath({a:path1, b:path2})
    m.run()




# Para testar os tipos de busca, troque no algoritmo para o nome da função que deseja testar
if __name__=='__main__':
    execucaoMaze(tamanho=80, possibilidadeCaminhos=100, algoritmo="dfs")