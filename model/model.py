import networkx as nx
from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()

    def buildGraph(self, anno):
        self._graph = nx.Graph()
        stati = DAO.getStati(anno)
        for stato in stati:
            self._graph.add_node(stato["nomeStato1"])
            self._graph.add_node(stato["nomeStato2"])
            self._graph.add_edge(stato["nomeStato1"], stato["nomeStato2"])

    def getComponentiConnesse(self):
        componenti = nx.dfs_tree(self._graph)
        return len(componenti)

    def getInfoStati(self):
        info = []
        for nodo in self._graph.nodes:
            vicini = len(list(self._graph.neighbors(nodo)))
            info.append(f"{nodo} -- {vicini} vicini.")
        info.sort()
        return info

    @staticmethod
    def getStati():
        return DAO.getAllStati()