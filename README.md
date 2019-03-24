# Backtrader Wrapper

It is a personal Backtrader wrapper to implement trading strategies.

Also, you can find some example strategies implemented.

# Cómo usar (python 3.7)

```sh
$ git clone https://github.com/bukosabino/wrapper-backtrader.git
$ cd wrapper-backtrader
$ pip install -r requirements.txt
$ python run.py
```

# Guide: Step by step

Estrategia a definir: Cruce de medias (SMA).

1 - Escribimos nuestra estrategia en un fichero python situado en la carpeta `strategies`.

2 - Importamos nuestra estrategia en `strategies.__init__.py`. Ejemplo:

from .nombre_fichero import NombreEstrategia

3 - En el `settings.py` modificamos la variable CONFIG['strategies'] para añadir nuestra estrategia.

4 - Ejecutamos el wrapper mediante:

python run.py

# Notes

El desarrollo de este proyecto tendrá continuación en: https://github.com/Python-para-Trading/wrapper-backtrader
