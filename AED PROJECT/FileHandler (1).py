
from model.ClientLinkedList import *
from model.DespesaLinkedList import *
from model.Despesa import *

import json
import datetime

class FileHandler:
    #Prof. Inês Almeida: Uma vez que não precisam de nenhum atributo especifico
     #Podem utilizar o construtor padrão, não sendo necessário reescrever o método __init__


    #Prof. Inês Almeida: Métodos de leitura e escrita    
    def save_data_to_json(self, clients):
        #Prof. Inês Almeida: o dicionário criado aqui é apenas um auxiliar para facilitar a escrita no ficheiro
        data = {
            'clients': []
        }
        
        #Prof. Inês Almeida: Armazena o cliente no json
        client_node = clients.head
        while client_node:
            client_data = {
                'username': client_node.get_element().get_username(),
                'nif': client_node.get_element().get_nif(),
                'password': client_node.get_element().get_password(),
                'monthly': client_node.get_element().get_monthly(),
                'expenses': []
            }

            expense_node = client_node.get_element().get_despesas().head
            while expense_node:
                expense_data = {
                    'categoria': expense_node.get_element().get_categoria(),
                    'descricao': expense_node.get_element().get_descricao(),
                    'valor': expense_node.get_element().get_valor(),
                    'data': expense_node.get_element().get_data().strftime('%Y-%m-%d')  # Prof.Inês Almeida: Converte date para string 
                }
                client_data['expenses'].append(expense_data)
                expense_node = expense_node.get_next_node()

            data['clients'].append(client_data)
            client_node = client_node.get_next_node()

        with open("data.json", 'w') as file:
            self.clean_file()
            json.dump(data, file)

    def read_data_from_json(self):
        with open("data.json", 'r') as file:
            data = json.load(file)

        clients = ClientLinkedList()

        for client_data in data['clients']:
            client = Cliente(client_data['username'], client_data['nif'], client_data['password'], int(client_data['monthly']))

            for expense_data in client_data['expenses']:
                despesa = Despesa(expense_data['categoria'], expense_data['descricao'], expense_data['valor'], datetime.datetime.strptime(expense_data['data'], '%Y-%m-%d'))
                client.add_despesa(despesa)

            clients.insert_last(client)

        return clients


    def clean_file(self):
        with open("data.json", 'w') as file:
            file.write("")