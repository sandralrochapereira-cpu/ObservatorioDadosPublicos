# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:48:26 2026

@author: sandr
"""

import requests
from bs4 import BeautifulSoup

url= "https://quotes.toscrape.com/"
registos=[]

try:
    resposta = requests.get(url, timeout =10)
    resposta.raise_for_status()
    soup = BeautifulSoup(resposta.text, "html.parser")
    for bloco in soup.find_all("div", class_="quote"):
        texto = bloco.select_one("span.text").get_text(strip=True)
        autor = bloco.select_one("small.author").get_text(strip=True)
        registos.append({"texto": texto, "autor": autor})
    print("Citações recolhidas: ", len(registos))
    for registo in registos:
        print(registo["autor"],"-",registo["texto"])
except requests.exceptions.RequestException as erro:
    print("Falha na consulta da página:", erro)
    
    
import csv 
with open("citacoes.csv", "w", newline="", encoding="utf-8-sig") as ficheiro:
    escritor = csv.DictWriter(ficheiro, fieldnames=["texto","autor"], delimiter=";")
    escritor.writeheader()        
    escritor.writerows(registos)
print("CSV de utilizadores criado")