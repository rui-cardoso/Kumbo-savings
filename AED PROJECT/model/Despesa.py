class Despesa:
    def __init__(self, categoria, valor, descricao, data):
        self.__categoria = categoria
        self.__valor = valor
        self.__descricao = descricao
        self.__data = data
        
        
    def get_categoria(self):
        return self.__categoria
        
    def set_categoria(self, nova_categoria):
        self.__categoria = nova_categoria
        
    def get_valor(self):
        return self.__valor
        
    def set_valor(self, novo_valor):
        self.__valor = novo_valor

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data = data
        
    def get_descricao(self):
        return self.__descricao
    
    def set_descricao(self, nova_descricao):
        self.__descricao = nova_descricao
    
        
    