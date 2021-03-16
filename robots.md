# Robots.txt

Un archivo robots.txt indica a los rastreadores de los buscadores qué páginas o archivos de tu sitio pueden solicitar y
cuáles no. Principalmente, se utiliza para evitar que las solicitudes que recibe tu sitio lo sobrecarguen; no es un
mecanismo para impedir que una página web aparezca en Google. Si lo que buscas es esto último, debes usar directivas
noindex o proteger esas páginas con contraseña.


```python
import os


from utils import robots_to_df
```

### En un archivo plano tenemos las 5 tiendas online a analizar. 
De dicho archivo plano obtenemos las urs y ejecutamos el script robots.py


```python
with open("data/dfg.txt", encoding="utf-8") as file:
    diputacion = [l.rstrip("\n") for l in file]
diputacion = diputacion[0]
diputacion
```




    'https://www.gipuzkoa.eus/es'



Vemos que algunas tiendas tienen el fichero robots.txt y otras no.


```python
robots_to_df(diputacion)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User-agent</th>
      <th>Status</th>
      <th>Pattern</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MauiBot</td>
      <td>Disallow</td>
      <td>/</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AhrefsBot</td>
      <td>Disallow</td>
      <td>/</td>
    </tr>
    <tr>
      <th>2</th>
      <td>DotBot</td>
      <td>Disallow</td>
      <td>/</td>
    </tr>
    <tr>
      <th>3</th>
      <td>SemrushBot</td>
      <td>Disallow</td>
      <td>/</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MJ12bot</td>
      <td>Disallow</td>
      <td>/</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/es/resultados-buscador</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/eu/bilaketaren-emaitzak</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*DLF_Bilatzailea</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*DLYCrossSiteRequestProxy-portlet</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*DLYServices-portlet</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*notifications-portlet</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*calendar-portlet</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*buscar</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*INSTANCE</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*combo</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*busqueda</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*bilaketa</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*galeria-bektoriala</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Seekport</td>
      <td>Disallow</td>
      <td>/*asset_publisher</td>
    </tr>
  </tbody>
</table>
</div>


