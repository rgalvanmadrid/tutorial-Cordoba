# tutorial-Cordoba
Tutorial en IATE y OAC 15 y 16 de abril de 2024

Diapositivas de intro: \
https://tinyurl.com/tutorial-Cordoba-RGM 

Dependencias: \
Python 3 con sus librerías científicas básicas (numpy, matplotlib) \
astropy (https://www.astropy.org) \
astroquery (https://astroquery.readthedocs.io) \
aplpy (https://aplpy.github.io) \
radio-beam (https://radio-beam.readthedocs.io) \
reproject (https://reproject.readthedocs.io) \
pyspeckit (https://pyspeckit.readthedocs.io) \
spectral-cube (https://spectral-cube.readthedocs.io) \
regions (https://astropy-regions.readthedocs.io) 


Además, el visualizador CARTA: \
https://cartavis.org

Notebooks: 

- RCrA-archive.ipynb: tutorial para explorar el archivo de ALMA de manera programática, bajar y desplegar algunas imágenes o cubos importantes y decidir si los datos disponibles son útiles o no.

  Nota: para la graficación hay un error de compatibilidad entre astropy 5.1.0 and matplotlib 3.7.0. 
Si se produce el error, actualizar a astropy>=5.1.1 
  
- continuum-spix.ipynb: tutorial para explorar y hacer análisis básico imágenes de continuo proporcionadas como un "data product" de un ALMA Large Program. 

- LineExample-ALMA-IMF.ipynb: tutorial para explorar y hacer análisis básico de cubos de línea espectral proporcionadas como un "data product" de un ALMA Large Program. 
