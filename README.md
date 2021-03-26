# Subastas de la Diputación

![alt text](https://images.pexels.com/photos/3664547/pexels-photo-3664547.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260)
 <a href="https://www.pexels.com/es-es/foto/hombre-de-camisa-azul-y-pantalon-marron-de-pie-junto-a-la-vaca-3664547/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels">Foto de carboxaldehyde en Pexels</a>

## Autores

        Oscar Rojo Martín         zumaia@uoc.edu
        Álvaro Rodríguez Pardo    alvarorp22@uoc.edu
        


## Contexto

El objetivo de este proyecto es el de obtener dos dataset de la Diputación Foral de Gipuzkoa con los datos de las subastas
pendientes y las realizadas, respectivamente.
Al final del proyecto dispondremos dos ficheros CSV donde se muestran todos los datos almacenados.

## La Diputacion

<img src="https://admin.uik.eus/uploads/thumbs/logocolaboradores_foto/1491/logo-vector-diputacion-de-gipuzkoa-monocromo.jpg" width="400" alt="Diputacion Foral de Gipuzkoa"/>  

<img src="https://egoitza.gipuzkoa.eus/documents/39465/42128/LogoSede2_eu.png" width="400" alt="Diputacion Foral de Gipuzkoa"/>  

## Los Dataset

Se encuentran almacenados en la carpeta data.

## robots.txt

Previo a la realización del trabajo, se ha generado un script para el análisis del fichero Robots.txt con objeto de conocer 
las páginas y ficheros que podemos solicitar y las que no.

Para ejecutar el script:

    $ python robots.py

El resultado del análisis de los 5 retails se puede consultar en el fichero **[robots.md](robots.md)**.

## Operativa

Los dos datasets obtenidos tienen como estructura común los siguientes campos:  

* URL
* Número
* Tipo
* Lugar
* Descripción
* Importe  
* Fecha  
* Procedimiento  
* Situación

Las formas de recopilar los datasets son muy parecidas y siguen el siguiente orden:  
1. Se obtiene la URL raíz de la tienda (contendida en un archivo plano).
2. Se sustituye la URL por la palabra tienda.
3. Se recorre la raíz inicial en busca de la URL "hijos".
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

Como se puede comprobar, muchas de las subastas que hay en el dataset que se ha obtenido han quedado desiertas. Habría que valorar si el motivo
fue el precio, las condiciones del inmueble o la falta de publicidad del evento.

## Licencia

Se ha elegido CC BY-NC-SA 4.0 ya que:
Esta [licencia](LICENSE.md) no permite un uso comercial de la obra original ni de las posibles obras derivadas. 
Además, la distribución de estas obras derivadas se debe hacer con una licencia igual a la que regula la obra original.

## Código

Para su correcta ejecución se recomienda:
1. Generar una carpeta

        $ mkdir -directorio
    
2. Generar un entorno virtual   
    en Linux  
    
        $ python3 -m venv /path/to/new/virtual/environment   
    
    en Windows
    
        c:\>c:\Python35\python -m venv c:\path\to\myenv
    
3. Instalar los módulos necesarios detallados en el fichero requirements.txt

        $ pip install requirements.txt
    
4. Ejecutar el scraping sobre las subastas de la Diputación:

        $ python diputacion.py
    
## Resultado final

![](data/resultado.png)

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4609730.svg)](https://doi.org/10.5281/zenodo.4609730)

