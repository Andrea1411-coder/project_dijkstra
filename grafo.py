import heapq
import networkx as nx
import math 
from data import TunjaData

class Grafo:
    def __init__(self, nodos: dict, aristas: list):
        self.nodos = nodos
        self.nombres = list(nodos.keys())
        self.n = len(self.nombres)
        self.indice = {n: i for i, n in enumerate(self.nombres)}


        # Lista de adyacencia: { nodo: [(vecino, peso), ...] }
        self.adyacencia = {n: [] for n in self.nombres}
 
        # Guarda las aristas para construir la matriz
        self._aristas = aristas
 
        for u, v, peso in aristas:
            self.adyacencia[u].append((v, peso))
            self.adyacencia[v].append((u, peso))