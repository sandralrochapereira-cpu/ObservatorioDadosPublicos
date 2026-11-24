# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:15:01 2026

@author: sandr
"""

import requests
pessoa_dic={}

# %%
url = "https://jsonplaceholder.typicode.com/users"

try:
    resposta = requests.get(url, timeout =10)
    resposta.raise_for_status()
    utilizadores = resposta.json()
    print("Total de utilizadores:", len(utilizadores))
    
    for pessoa in utilizadores:
        print(pessoa["name"], "-", pessoa["email"])
        pessoa_dic[pessoa["name"]]= pessoa["email"]
         
                
    print("Registo não encontrado")
        
except requests.exceptions.RequestException as erro:
    print("Não foi possível consultar a API", erro)

import csv 
with open("utilizadores.csv", "w", newline="", encoding="utf-8-sig") as ficheiro:
    escritor = csv.DictWriter(ficheiro, fieldnames=["nome","email"], delimiter=";")
    escritor.writeheader()
    for pessoa in utilizadores:
        escritor.writerow({"nome":pessoa["name"], "email": pessoa["email"]})
print("CSV de utilizadores criado")
