# Subastas de la Diputación.

![](data/asim-z-kodappana-ks21cxRTzSo-unsplash.jpg)
Photo by <a href="https://unsplash.com/@jordannix?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jordan Nix</a> on <a href="/s/photos/baby-clothes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

## Autores

        Oscar Rojo Martín         zumaia@uoc.edu
        Álvaro Rodríguez Pardo    alvarorp22@uoc.edu
        


## Contexto

El objeto de este proyecto es el de obtener de la Diputación Foral de Gipuzkoa, 2 dataset con los datos de las subastas
a realizar y las ya realizasdas.
Al final del proyecto obtendremos 2 ficheros csv donde se muestran todos los datos almacenados.

## La Diputacion

<img src="https://admin.uik.eus/uploads/thumbs/logocolaboradores_foto/1491/logo-vector-diputacion-de-gipuzkoa-monocromo.jpg" width="400" alt="Diputacion Foral de Gipuzkoa"/>  

<img src="https://egoitza.gipuzkoa.eus/documents/39465/42128/LogoSede2_eu.png" width="400" alt="Diputacion Foral de Gipuzkoa"/>  

## Los dataset

Se encuentran almacenados en la carpeta data.

## Robots.txt

Previa a la realización del trabajo, he generado un script para el análisis del fichero Robots.txt al objeto de conocer 
las páginas y fichero podemos solicitar y cuales no.

Para ejecutar el script:

    $ python robots.py

El resultado del análisis de los 5 retails se puede consultar en el fichero **[robots.md](robots.md)**

## Operativa:  
Basicamente los 2 datasets obtenidos tienen como estructura comun los siguientes campos:  

* Url
* Numero
* Tipo
* Lugar
* Descripción
* Importe  
* Fecha  
* Procedimiento  
* Situación

La forma de recopiar los datasets son muy parecidas y en el siguiente orden:  
1. Obtendo la url raiz de la tienda (contendida en un archivo plano)
2. Subtituyo la url por la palabra tienda  
3. Recorro la raiz inicial en busca de url "hijos"  
4. Recopilo los diferentes URL en una lista que la limpio de datos innecesarios y elementos duplicados  
5. Recorro la lista de hijos en busca de nuevas url
6. Recopilo las nuevas url y hago nuevamente una limpieza de la nueva lista.
7. De esta última lista de url donde se detallan cada uno de los productos, realizo el scraping
8. Genero un diccionario seleccionando los campos que más me interesan.
9. Por último convierto el diccionario en un dataframe y este en un csv.

En todas las transformaciones y con el fin de preservar la url y el nombre comercial de la empresa retail,
aplico el pundo 2

## Propietarios de los datos

https://www.gipuzkoa.eus/es/

## Inspiración. 

El presente proyecto la primera publicación que realizó la Diputación Foral de Gipuzkoa en los portales inmobiliarios de
internet como "Idealista" y "Fotocasa" donde informaban de las subastas.  

Como se puede comprobar en el dataset obtenido, muchas de las subastas quedaron desiertas. Habría que valorar si el motivo
fue el precio, las condiciones del inmueble o la falta de publicidad del evento.

## Licencia

He elegigido CC BY-NC-SA 4.0 ya que:
Esta [licencia](LICENSE.md) no permite un uso comercial de la obra original ni de las posibles obras derivadas. 
Además, la distribución de estas obras derivadas se debe hacer con una licencia igual a la que regula la obra original.

## Los dataset
10. Dataset. Publicación del dataset en formato CSV en Zenodo (obtención del DOI)
con una breve descripción.

## Operativa.

Para su correcta ejecución recomiendo:
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
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4604713.svg)](https://doi.org/10.5281/zenodo.........)
