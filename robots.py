"""
Un archivo robots.txt indica a los rastreadores de los buscadores qué páginas o archivos de tu sitio pueden solicitar y
cuáles no. Principalmente, se utiliza para evitar que las solicitudes que recibe tu sitio lo sobrecarguen; no es un
mecanismo para impedir que una página web aparezca en Google. Si lo que buscas es esto último, debes usar directivas
noindex o proteger esas páginas con contraseña.
"""


import os


from utils import robots_to_df

cwd = os.getcwd()
print(cwd)

with open("data/dfg.txt", encoding="utf-8") as file:
    diputacion = [l.rstrip("\n") for l in file]
diputacion = diputacion[0]



print("\n")
print(diputacion)
print("\n")
print(robots_to_df(diputacion))



