# Subastas de la Diputación.

![](data/asim-z-kodappana-ks21cxRTzSo-unsplash.jpg)
Photo by <a href="https://unsplash.com/@jordannix?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jordan Nix</a> on <a href="/s/photos/baby-clothes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

## Autores

        Oscar Rojo Martín         zumaia@uoc.edu
        Álvaro Rodríguez Pardo    alvarorp22@uoc.edu
        


## Contexto

El objetivo de este proyecto es el de obtener dos dataset de la Diputación Foral de Gipuzkoa con los datos de las subastas
a realizar y las ya realizadas.
Al final del proyecto obtendremos 2 ficheros CSV donde se muestran todos los datos almacenados.

## La Diputacion

<img src="https://admin.uik.eus/uploads/thumbs/logocolaboradores_foto/1491/logo-vector-diputacion-de-gipuzkoa-monocromo.jpg" width="400" alt="Diputacion Foral de Gipuzkoa"/>  

<img src="https://egoitza.gipuzkoa.eus/documents/39465/42128/LogoSede2_eu.png" width="400" alt="Diputacion Foral de Gipuzkoa"/>  

## Los dataset

Se encuentran almacenados en la carpeta data.

## Robots.txt

Previo a la realización del trabajo, se ha generado un script para el análisis del fichero Robots.txt con objeto de conocer 
las páginas y ficheros que podemos solicitar y las que no.

Para ejecutar el script:

    $ python robots.py

El resultado del análisis de los 5 retails se puede consultar en el fichero **[robots.md](robots.md)**.

## Operativa

Basicamente los dos datasets obtenidos tienen como estructura común los siguientes campos:  

* URL
* Número
* Tipo
* Lugar
* Descripción
* Importe  
* Fecha  
* Procedimiento  
* Situación

La forma de recopilar los datasets son muy parecidas y en el siguiente orden:  
1. Se obtiene la URL raiz de la tienda (contendida en un archivo plano).
2. Se sustituye la URL por la palabra tienda.
3. Se recorre la raiz inicial en busca de URL "hijos".
4. Se recopilan las diferentes URLs en una lista que se ha de limpiar de datos innecesarios y elementos duplicados.
5. Se recorre la lista de hijos en busca de nuevas URLs.
6. Se recopilan las nuevas URLs y se realiza una vez más una limpieza de la nueva lista.
7. De esta última lista de URLs donde se detallan cada uno de los productos, se realiza el scraping.
8. Se genera un diccionario seleccionando los campos que más nos interesan.
9. Por último, se convierte el diccionario en un dataframe y este en un archivo CSV.

En todas las transformaciones, con el fin de preservar la URL y el nombre comercial de la empresa retail,
se aplica el punto 2.

## Propietarios de los datos

https://www.gipuzkoa.eus/es/

## Inspiración 

El presente proyecto se inspira en la primera publicación que realizó la Diputación Foral de Gipuzkoa en los portales inmobiliarios de
internet como "Idealista" y "Fotocasa", donde se informaba de las subastas.  

Como se puede comprobar, muchas de las subastas que hay en el dataset obtenido quedaron desiertas. Habría que valorar si el motivo
fue el precio, las condiciones del inmueble o la falta de publicidad del evento.

## Licencia

Se ha elegido CC BY-NC-SA 4.0 ya que:
Esta [licencia](LICENSE.md) no permite un uso comercial de la obra original ni de las posibles obras derivadas. 
Además, la distribución de estas obras derivadas se debe hacer con una licencia igual a la que regula la obra original.

## Los dataset

10. Dataset. Publicación del dataset en formato CSV en Zenodo (obtención del DOI)
con una breve descripción.

## Operativa

Para su correcta ejecución se recomienda:
1. Generar una carpeta

        $ mkdir -directorio
    
2. Generar un entorno virtual   
    en linux  
    
        $ python3 -m venv /path/to/new/virtual/environment   
    
    en windows
    
        c:\>c:\Python35\python -m venv c:\path\to\myenv
    
3. Instalar los módulos necesarios detallados en el fichero requirements.txt

        $ pip install requirements.txt
    
4. Ejecutar cada un de los ejecutables según la tienda

        $ python tienda_#.py
    
    donde # es el número de tienda, desde 0 hasta 1.
    
## El resultado final

![](data/resultado.png)




## EL DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4609730.svg)](https://doi.org/10.5281/zenodo.4609730)

