import flet as ft

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
        self._view._ddStati.disabled = False
        self._view._btnStatiRaggiungibili.disabled = False
        self._view.update_page()

    def fillDD(self):
        stati = self._model.getStati()
        for stato in stati:
            self._view._ddStati.options.append(ft.dropdown.Option(key=stato.StateNme, data=stato))
        self._view.update_page()

    def handleStatiRaggiungibili(self, e):
        statoScelto = self._view._ddStati.value
        statiRaggiungibili = self._model.getStatiRaggiungibili(statoScelto)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Elenco stati raggiungibili a partire da {statoScelto}:"))
        for stato in statiRaggiungibili:
            self._view._txt_result.controls.append(ft.Text(stato))
        self._view.update_page()