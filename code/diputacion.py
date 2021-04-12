#!/usr/bin/env python
# coding: utf-8

# Cargamos las librerías que utilizaremos
from bs4 import BeautifulSoup
import pandas as pd
import requests
from functools import reduce


# Cargamos el archivo .txt que contiene las urls
with open("data/diputacion.txt", encoding="utf-8") as file:
    diputacion = [l.rstrip("\n") for l in file]


# Seleccionamos dichas urls
subastas = diputacion[0]
celebradas = diputacion[1]


# Empezamos con el web scraping de las subastas pendientes

# Primer web scraping:
headers = {
    "user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

r = requests.get(subastas, headers=headers)
soup = BeautifulSoup(r.content, "html5lib")

# Generamos una lista vacia
url_data = []

# Mediante try(), se recogerán las subastas pendientes en caso de haberlas, y si no las hay,
# con except() generaremos un mensaje que imprima por pantalla un mensaje avisando de que
# no existen subastas pendientes
try:
    for table in soup.find("table", {"class": "footable stripe dataTable no-footer no-basicDataTable"}):
        for rows in table.find("tr"):
            cols = table.find_all("tr")
            f = len(cols)
            for i in range(f):
                a = cols[i].get_text().strip()
                a = a.replace("\n", "")
                a = a.replace("\t", " ")
                url_data.append(a)

        lista = url_data[0:f]
        lista = [i.split() for i in lista]

        # Convertimos la lista en dataframe
        resumen = pd.DataFrame(lista, columns=lista[0])[1:]

        headers = {
            "user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        r = requests.get(subastas, headers=headers)
        soup = BeautifulSoup(r.content, "html5lib")
        url_subastas = []

        table = soup.find("table", {"class": "footable stripe dataTable no-footer no-basicDataTable"})
        rows = table.findAll("a")
        for tr in rows:
            links = tr.get("href")
            url_subastas.append(links)

        # Hacemos un nuevo web scraping
        # Generamos una lista vacia
        total_url = []
        headers = {
            "user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        for i in url_subastas:
            r = requests.get(i, headers=headers)
            soup = BeautifulSoup(r.content, "html5lib")
            # Generamos una nueva lista
            total = []
            # Buscamos "span class: lora-font-book" dentro del código
            resulta = soup.findAll("span", attrs={"class": "lora-font-book"})
            # iteramos para generar una lista
            for link in resulta:
                text = link.get_text()
                total.append(text)
            # añadimos a la nueva lista la url
            total.insert(0, i)
            # añadimos total la lista general
            total_url.append(total)

        # Convertimos la lista de las subastas pendientes en un dataframe
        subastas_pendientes = pd.DataFrame(
            total_url,
            columns=(
                "url",
                "numero",
                "tipo",
                "lugar",
                "descripcion",
                "importe",
                "fecha",
                "procedimiento",
                "situacion",
            ),
        )
        # Guardamos el dataframe en un archivo CSV
        subastas_pendientes.to_csv("data/subastas_pendientes.csv")
        
except:
    print("No hay subastas pendientes")

    

# Continuamos con el web scraping de las subastas realizadas

# Primer web scraping
r = requests.get(celebradas, headers=headers)

soup = BeautifulSoup(r.content, "html5lib")


url_celebradas = []
# buscamos "table, class:footable stripe dataTable no-footer no-basicDataTable"
table = soup.find(
    "table", {"class": "footable stripe dataTable no-footer no-basicDataTable"}
)
# buscamos en table "a"
rows = table.findAll("a")
# iteramos donde se encuentre los valores del código "a"
for tr in rows:
    # obtener los link tras "a href"
    links = tr.get("href")
    # añadimos a la lista creada
    url_celebradas.append(links)


headers = {
    "user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
r = requests.get(celebradas, headers=headers)
soup = BeautifulSoup(r.content, "html5lib")
# iteramos donde se encuentre los valores del código "a"
for link in soup.find_all("a"):
    # obtener los link tras "a href"
    text = link.get("href")
    # añadimos a la lista creada
    url_data.append(text)


# Seleccionamos las que comienzan por ...
start_letter = "https://www.gipuzkoa.eus/es/web/ogasuna/subastas/celebradas?"
data_total_url = [k for k in url_data if start_letter in k]

# Guardamos en otra lista las urls sin repeticiones
res_data_total_url = []
for i in data_total_url:
    if i not in res_data_total_url:
        res_data_total_url.append(i)
# Hacemos una selección
rest_total = res_data_total_url[1:]

# Insertamos la url principal
rest_total.insert(0, celebradas)

# Obtenemos todas las urls
total_total = []

for i in rest_total:
    # url = input("Enter a website to extract the URL's from: ")
    r = requests.get(i, headers=headers)
    soup = BeautifulSoup(r.content, "html5lib")
    # Generamos una lista vacia
    url_celebradas = []
    table = soup.find("table", {"class": "footable stripe dataTable no-footer no-basicDataTable"})
    rows = table.findAll("a")
    # Iteramos
    for tr in rows:
        links = tr.get("href")
        url_celebradas.append(links)
    # vamos añadiendo los datos obtenidos a la nueva lista
    total_total.append(url_celebradas)


# Unificamos las listas concatenadas en una
single_list = reduce(lambda x, y: x + y, total_total)

# Guardamos en una nueva lista las urls sin repeticiones
# Generamos una lista vacia
res_res_data_total_url = []
# realizamos un loop para revisar si hay duplicados
for i in single_list:
    if i not in res_res_data_total_url:
        res_res_data_total_url.append(i)


# Hacemos un nuevo web scraping con la lista de urls sin repeticiones
# Generamos una lista vacia
total_url = []
headers = {
    "user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
# Iteramos por todos los elementos de la lista.
for i in res_res_data_total_url:
    r = requests.get(i, headers=headers)
    soup = BeautifulSoup(r.content, "html5lib")
    # Generamos una lista vacia
    total = []
    resulta = soup.findAll("span", attrs={"class": "lora-font-book"})
    # iteramos por resulta
    for link in resulta:
        text = link.get_text()
        total.append(text)
    # En la lista insertamos la url.
    total.insert(0, i)
    # Añadimos total en total_url
    total_url.append(total)


# Convertimos la lista de las subastas realizadas en un dataframe
subastas_resueltas = pd.DataFrame(
    total_url,
    columns=(
        "url",
        "numero",
        "tipo",
        "lugar",
        "descripcion",
        "importe",
        "fecha",
        "procedimiento",
        "situacion",
    ),
)

# Guardamos el dataframe en un archivo CSV
subastas_resueltas.to_csv("data/subastas_resueltas.csv")
