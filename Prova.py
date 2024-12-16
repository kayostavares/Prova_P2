class Grafo:
    def __init__(self):
        self.adjacencia = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A'],
            'D': ["NÃO SEI TBM"],
        }

    #ADICIONEI POR VIA DAS DUVIDAS DEVIDO A UM ERRO NAO SOLUCIONADO DEVIDO AO ANUNCIADO ERRADO

    def verificar_ciclos(self):
        visitado = set()
        pilha_recursao = set()

        def dfs(v):
            if v in pilha_recursao:
                return True
            if v in visitado:
                return False
            visitado.add(v)
            pilha_recursao.add(v)

            for vizinho in self.adjacencia.get(v, []):
                if dfs(vizinho):
                    return True

            pilha_recursao.remove(v)
            return False

        for vertice in self.adjacencia:
            if dfs(vertice):
                return True
        return False

    def exibir_lista_adjacencia(self):
        for vertice, arestas in self.adjacencia.items():
            print(f"{vertice} -> {', '.join(arestas)}")

grafo = Grafo()

print("Lista de Adjacência do Grafo:")
grafo.exibir_lista_adjacencia()

if grafo.verificar_ciclos():
    print("O grafo contém ciclos pois o um ciclo entre a->b->c->a")
else:
    print("O grafo não contém ciclos.")
