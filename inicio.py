# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:26:20 2023

@author: ACER
"""

import pandas as pd
def comienzo():
    # Nombre de tu archivo CSV
    csv_filename = "iris.csv"
    
    # Nombre de usuario y token de acceso a tu cuenta de GitHub
    username = "joseirt"
    access_token = "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"
    
    # Nombre del repositorio en GitHub (solo el nombre del repositorio)
    repo_name = "proyecto"
    
    class IteradorIris:
        def __init__(self, csv_filename):
            self.df = pd.read_csv(csv_filename)
            self.index = 0
    
        def __iter__(self):
            return self
    
        def __next__(self):
            if self.index < len(self.df):
                data = self.df.iloc[self.index]
                self.index += 1
                return data.to_dict()  # Convertir la fila a un diccionario
            else:
                raise StopIteration("No hay más datos disponibles")
    return csv_filename,repo_name,username,access_token, IteradorIris  
    
