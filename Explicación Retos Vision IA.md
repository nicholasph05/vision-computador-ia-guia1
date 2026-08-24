**Reto 1**



La matriz está creada e inicializada con números aleatorios, cada lista interna representa una fila de la imagen

y cada número representa la intensidad del pixel de la imagen entre 0(negro) y 255(blanco).

\----------------------------------------------------------------------------------------------------------------------------------------

**-Primero recorremos los 1.000.000 de valores y obtenemos mínimo, máximo y suma.**



**La media corresponde conceptualmente a:**



media = suma de todos los valores / cantidad de valores



Después necesitamos otro recorrido porque para calcular la desviación estándar primero debemos conocer la media.



**Calculamos qué tan separado está cada píxel de esa media:**



diferencia = valor - media



**elevamos esa diferencia al cuadrado:**



diferencia \*\* 2



**calculamos la varianza y finalmente hacemos:**



math.sqrt(varianza)



para obtener la desviación estándar.



\-Aunque los valores individuales de la matriz son aleatorios, al generar una cantidad muy grande de datos con distribución uniforme entre 0 y 255, la media tiende a 127.5 y la desviación estándar a aproximadamente 73.9.



\------------------------------------------------------------------------------------------------------------------------------------------

**¿Qué hace reshape?**



Actualmente tenemos:



vector\_numpy

↓

1.000.000 elementos





\[125, 27, 243, 18, 90, ...]



Con:



vector\_numpy.reshape(1000, 1000)



NumPy los vuelve a organizar como:



1000 filas × 1000 columnas



y cada número pasa a representar un píxel.



**Como usamos:**



cmap="gray"



**se interpreta así:**



0   → negro

...

127 → gris aproximadamente

...

255 → blanco





