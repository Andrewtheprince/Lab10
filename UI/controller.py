import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        if anno == "":
            self._view._txtAnno.value = ""
            self._view.create_alert("Devi inserire un valore!")
            return
        try:
            anno = int(anno)
        except ValueError:
            self._view._txtAnno.value = ""
            self._view.create_alert("Devi inserire un valore numerico !")
            return
        if anno < 1816 or anno > 2016:
            self._view._txtAnno.value = ""
            self._view.create_alert("Devi inserire un valore numerico tra 1816 e 2016!")
            return
        self._model.buildGraph(anno)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getComponentiConnesse()} componenti connesse."))
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))
        infoStati = self._model.getInfoStati()
        for info in infoStati:
            self._view._txt_result.controls.append(ft.Text(info))
        self._view.update_page()

    def fillDD(self):
        stati = DAO.getAllStati()
        for stato in stati:
            self._view._ddStati.options.append(ft.dropdown.Option(key=stato.StateNme, data=stato))
        self._view.update_page()

    def handleStatiRaggiungibili(self, e):
        print(self._view._ddStati.value)