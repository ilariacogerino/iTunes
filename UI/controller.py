import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        durata = self._view._txtInDurata.value
        if durata is None or durata == '' or durata.isdigit()==False:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f'Inserire un valore valido!!', color='red'))
            self._view.update_page()
            return
        durata = int(durata)
        self._model.buildGraph(durata)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Grafo creato!'))
        self._view.txt_result.controls.append(ft.Text(f'# Vertici: {self._model.getNumNodes()}'))
        self._view.txt_result.controls.append(ft.Text(f'# Archi: {self._model.getNumEdges()}'))

        self.fillddAlbum()

        self._view.update_page()

    def fillddAlbum(self):
        album = self._model.getAllNodes()
        for a in album:
            self._view._ddAlbum.options.append(ft.DropdownOption(text=a.Title, key=a.AlbumId))


    def getSelectedAlbum(self, e):
        pass

    def handleAnalisiComp(self, e):
        album = self._view._ddAlbum.value
        print(album)
        map = self._model.getIdMap()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Componente connessa - {map[int(album)].Title}'))
        self._view.txt_result.controls.append(ft.Text(f'Dimensione componente: {self._model.getNumNeighbors(album)}'))
        durataTot = self._model.getSumAlbumsTime(album)
        self._view.txt_result.controls.append(ft.Text(f'Durata componente: {round(durataTot, 4)}'))

        self._view.update_page()


    def handleGetSetAlbum(self, e):
        pass