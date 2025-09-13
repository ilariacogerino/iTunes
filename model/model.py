import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._idMap = {}

    def buildGraph(self, tempo):
        self._nodes = DAO.getAlbumsPerDurata(tempo)
        self._graph.add_nodes_from(self._nodes)
        for node in self._nodes:
            self._idMap[node.AlbumId] = node
        self._edges = DAO.getAllEdges(self._idMap)
        self._graph.add_edges_from(self._edges)


    def getNeighbors(self, albumId):
        album = self._idMap[int(albumId)]
        return nx.neighbors(self._graph, album)

    def getSumAlbumsTime(self, albumsId):
        albums = self.getNeighbors(albumsId)
        sum = self._idMap[int(albumsId)].Time
        for a in albums:
            sum += a.Time
        return sum

    def getNumNeighbors(self, albumId):
        album = self._idMap[int(albumId)]
        return len(list(nx.neighbors(self._graph, album)))

    def getComponentiConnesse(self, idAlbum):
        album = self._idMap[int(idAlbum)]
        return len(nx.number_connected_components(self._graph))+1

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getAllNodes(self):
        return self._nodes

    def getAllEdges(self):
        return self._edges

    def getIdMap(self):
        return self._idMap
