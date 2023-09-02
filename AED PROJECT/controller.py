from view import *

class Controller:
    def __init__(self, master):
        self.view = View(master)
        
        
    def adicionar_despesa(self):
        categoria = self.view.combo_categorias.get()
        descricao = self.view.descrição_da_despesa1.get()
        valor = self.view.categorias2.get()
        pass