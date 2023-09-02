class Cliente:
    def __init__(self, nome, password, nif):
        self.__nome = nome
        self.__password = password
        self.__nif = nif

    def get_nome(self):
        return self.__nome
        
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        
    def get_password(self):
        return self.__password
        
    def set_password(self, nova_password):
        self.__password = nova_password

    def get_nif(self):
        return self.__nif

    def set_nif(self,nif):
        self.__nif = nif





