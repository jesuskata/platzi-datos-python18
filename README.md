# Curso de Ingeniería de Datos con Python

- [Curso de Ingeniería de Datos con Python](#curso-de-ingenier%C3%ADa-de-datos-con-python)
  - [¿Qué es la Ciencia e Ingeniería de Datos?](#%C2%BFqu%C3%A9-es-la-ciencia-e-ingenier%C3%ADa-de-datos)
  - [Roles](#roles)
  - [Configuración del ambiente](#configuraci%C3%B3n-del-ambiente)
  - [Jupyter Notebook](#jupyter-notebook)
  - [Tipos de datos](#tipos-de-datos)
  - [Fuentes de datos](#fuentes-de-datos)
    - [Links de fuentes de datos](#links-de-fuentes-de-datos)
  - [ETL (Extract Transform Load)](#etl-extract-transform-load)
  - [Introducción a las tecnologías web](#introducci%C3%B3n-a-las-tecnolog%C3%ADas-web)
  - [Realizando solicitudes HTTP con Python](#realizando-solicitudes-http-con-python)

## ¿Qué es la Ciencia e Ingeniería de Datos?

La _Ciencia de Datos_ es la disciplina que se encarga de _extraer conocimiento de los datos disponibles_. Casi siempre cuando te realizas una pregunta sobre datos estas fuentes se encuentra escondidas, ocultas o de difícil acceso. A nuestro alrededor hay datos en tu computadora, mesa, reloj, etc.

> Los datos están por todas partes.

La Ciencia de datos es _multidisciplinaria_. A diferencia de muchos otros ámbitos profesionales dentro del mundo de la tecnología, cuando hablamos de un científico de datos es una persona que sabe de matemáticas, ingeniería de software y sabe de negocios.

Se apoya en la _Computer science_, _Matemáticas_(Regresiones e Inferencias),

También se auxilia de:

- Bases de Datos
  - SQL y NoSQL
- Análisis de texto y procesamiento de lenguaje natural
- Análisis de redes
- Visualización de datos
- Machine learning e Inteligencia Artificial
- Análisis de señales digitales
- Análisis de datos en la nube(Big Data)

## Roles

Existen por lo menos tres diferentes roles para tener un _pipeline_ completo de ciencia de datos. Este curso trata sobre el primer rol:

- __Data engineer__
  - Se encarga de obtener los datos
  - Limpiarlos y estructurarlos para posterior análisis
  - Crear pipelines de análisis automatizado
  - Utilización de herramientas en la nube
  - Análisis descriptivo de los datos.

- __Data scientist__
  - Una vez tiene los datos se encarga de generar el análisis matemático de ellos
  - Encuentra las relaciones entre las variables, las correlaciones, las causas
  - Genera los modelos predictivos y prescriptivos.

- __Machine Learning engineer__
  - Se encarga de llevar las predicciones a escala
  - Subirlos a la nube
  - En la nube, generar muchas predicciones
  - Se encarga de mantener la calidad del modelo.

## Configuración del ambiente

_Anaconda_ es una instalación de _Python_ que ya trae preinstalado todos los paquetes necesarios para tu labor en la Ciencia de Datos, tiene más de 1400 paquetes. Nos permite configurar ambientes virtuales para poder utilizar diferentes versiones de nuestros paquetes.

```bash
conda --version # para conocer la versión y saber que lo tenemos instalado
conda --help # nos da todos los comandos que podemos usar.
conda list # nos lista todos los paquetes que Anaconda instaló.
```

Una buena práctica es generar un ambiente virtual por cada proyecto, los ambientes virtuales nos permiten generar varios proyectos con diferentes versiones de la librería sin generarnos errores de compatibilidad. Tradicionalmente en Python se utiliza `virtualenv`.

```bash
conda create --name [nombre-del-proyecto] [librerías-a-usar]
conda create --name platzi-data beautifulsoup4 requests numpy pandas matplotlib yaml
```

```bash
source activate platzi-data # Para activar
source deactivate # Para salir

conda env list # nos muestra los ambientes virtuales que tenemos
conda remove --name [nombre-del-proyecto] --all # eliminar nuestro entorno virtual con todos nuestros paquetes
```

## Jupyter Notebook

Algo interesante que tenemos con _Anaconda_ es que nos trae _Jupyter Notebooks_.

Jupyter Notebooks es un __entorno de programación__ en el cual podemos mezclar ejecución de _código en vivo_, _visualizaciones_ y añadir _markdown_.

Para inicializar nuestro servidor de jupyter, escribimos en el command line: `jupyter notebook`.

Jupyter Notebook tiene diferentes tipos de celdas en las cuales podemos escribir código o markdown. Si queremos ejecutar nuestro código hacemos `ctrl + enter` y si queremos ejecutar y añadir una nueva celda `shift + enter`.

Jupyter Notebook tiene dos modalidades, la modalidad de __edición__ y __navegación__.

## Tipos de datos

Los datos vienen en mucha formas y estas formas las podemos clasificar de diferentes maneras, permitiéndonos poder aplicar técnicas distintas a cada uno de los tipos de datos.

Los primeros datos son los primitivos.

- int,
- str,
- bool,
- float,
- hex,
- oct,
- datetime,
- objetos especiales

```python
from datetime import datetime

integer_type = 42
float_type = 3.14159
bool_type = False
hex_type = 0xff
oct_type = 0o23
today = datetime.now()
str_type = 'Jesus'
```

Tenemos clasificaciones ulteriores como:

- Los datos estructurados: son los más fáciles de acceder
  - Bases de datos
  - Data warehouses

![Tabla de base de datos MySQL](assets/mysql_table_example.png)

- Semi estructurados: son con los que podemos utilizar APIs
  - json API
  - Datos tabulares (csv, excel)
- no estructurados: la mayoría de datos que vamos a tener disponibles están clasificados aquí
  - HTML
  - Texto libre
  - Currículums vitae
  - Imágenes, audio, social media
  - Datos científicos

![Markup en HTML](assets/html_markup_example.png)

- Cualitativos vs cuantitativos
- Tiempo real vs históricos

## Fuentes de datos

- __Web__

Es una mina enorme con datos financieros, de startups, del clima, precipitación fluvial, astronómicos, de negocios, etc.

- __APIs__

Endpoints que viven en la web y nos devuelven JSON. Por ejemplo, la API de twitter, google, facebook.

- __User Analytics__

Son el comportamiento del usuario dentro de nuestra aplicaciones, algo similiar a los que nos ofrece Google Analytics.

- __IoT__

Se ha vuelto una mina espectacular en los últimos años. Como automóviles.

### Links de fuentes de datos

- [El Pais](https://elpais.com/elpais/portada_america.html)
- [Google Cloud Platform](https://console.cloud.google.com/apis/library)
- [Datos Abiertos de México](https://datos.gob.mx/)
- [Dataset Search by Google](https://toolbox.google.com/datasetsearch)
- [Data Catalog for Analysis](https://data.world/)
- [Kaggle, for Data Science](https://www.kaggle.com/)

## ETL (Extract Transform Load)

__Extract__: Es el proceso de lectura de datos de diversas fuentes

- Base de datos
- CRM
- Archivos CSV
- Datasets públicos

__Transform__: En este momento cuando nosotros tenemos que transformar los datos, tenemos que identificar datos faltantes o datos erróneos o una edad negativa. En esta etapa donde tenemos que identificar todos los problemas y solucionarlos.

- Limpieza
- Estructurado
- Enriquecimiento.

__Load__: Una vez transformados debemos insertarlos en el data warehouse

- Depende del tipo de solución que se haya escogido

![ETL](assets/etl-python.jpg)

## Introducción a las tecnologías web

Las tecnologías web en principio podemos pensarlas como el internet, pero el internet es mucho más grande, es la _red de redes_, la forma en la que millones de computadores se conectan entre ellas para _transferirse información_.

El internet también se compone de otros pedazos como:

- Telefonía(voip),
- Mail(pop3, imap),
- Compartir archivos(ftp).

El internet es una red que une varias redes públicas, privadas, académicas, de negocios, de gobiernos, etc.

La web específicamente es un espacio de información en el cual varios documentos(y otros recursos web) se pueden acceder a través de URLs y vínculos(links). La comunicación se da a través del protocolo HTTP.

Elementos básicos de la web:

- __HTML__: nos da la estructura de la información. Es un lenguaje para anotar pedazos de información para que el navegador o otros tipos de programa puedan interpretar que tipo de información se encuentra ahí.
- __CSS__: nos permite darle colores, arreglar el texto y añadir diferentes elementos de presentación.
- __Javascript__: nos permite añadir interactividad y cómputo a nuestra web.
- __JSON__: Simplemente es una forma de transmitir datos entre servidores y clientes. Es la forma estándar en las que en la web y las aplicaciones se comunican con los servidores backend.

Un link interesante para los sitios SPA, sería [Puppeteer](https://developers.google.com/web/tools/puppeteer/), ya que al ser rendereado por JavaScript, nuestro `scrapping` a veces puede que nos traiga sitios "vacíos".

## Realizando solicitudes HTTP con Python

Para poder experimentar con la web necesitamos un método programático para solicitar _URLs_ y obtener _HTML_.

__Requests__: Nos permite generar solicitudes a la web dentro de Python y utilizar los diferentes verbos `HTTP`, normalmente utilizaremos el método `GET` porque vamos a traer datos.

Algunos ejemplos de verbos HTTP:

- GET
- POST
- PUT
- DELETE
- PATCH
- OPTIONS

```bash
requests.get('url') # para hacer una solicitud a la web y nos devolverá un objeto response
```

Todas las solicitudes _HTTP_ tienen _metadatos_ para que los diferentes sistemas y computadoras puedan entender de qué va la solicitud.

Algunos de los códigos de estado del protocolo HTTP:

- 200 : OK - Petición correcta.
- 400 : Bad request - Petición incorrecta.
- 404 : Not found - Recurso no encontrado.

Estos códigos estan categorizados en los siguientes grupos:

- 1xx : Respuestas informativas (Ej: 100, 101, 102, etc.)
- 2xx : Peticiones correctas (Ej: 200, 201, 202, etc.)
- 3xx : Redirecciones (Ej: 300, 301, 302, etc.)
- 4xx : Errores en el lado del cliente (Ej: 400, 401, 402, etc.)
- 5xx : Errores en el lado del servidor (Ej: 500, 501, 502, etc.)

Puedes ver la lista en este [link](https://es.wikipedia.org/wiki/Anexo:C%C3%B3digos_de_estado_HTTP)

Un ejemplo del uso de una librería de Python llamada `requests`:

```python
import requests

response = requests.get('https://platzi.com')

response? # Nos da una respuesta con información mínima del tipo de contenido
response?? # Nos extiende la respuesta de la clase con su contenido

print(dir(response)) # Nos da todos los métodos que podemos usar en response

# ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

print(response.status_code) # Nos devuelve el status code (en este caso 200)

print(response.headers) # Nos devuelve los headers de la página

# {'Date': 'Tue, 06 Nov 2018 17:04:21 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d1b51196c1cf6dbe852e2ab7c341fd1761541523860; expires=Wed, 06-Nov-19 17:04:20 GMT; path=/; domain=.platzi.com; HttpOnly, entry_path="/"; expires=Tue, 06-Nov-2018 17:54:21 GMT; Max-Age=3000; Path=/, s=s723u4hzyyae5eij27jr2qhaivflws65; Domain=.platzi.com; expires=Tue, 20-Nov-2018 17:04:21 GMT; HttpOnly; Max-Age=1209600; Path=/; Secure, csrftoken=KH1rPdE3CzxwYgrlUQsV4yoAQIoVQmVPgOTo3AHGrEsmW5OldBBGMegvJw6UI6d1; expires=Tue, 05-Nov-2019 17:04:21 GMT; Max-Age=31449600; Path=/', 'Content-Language': 'es', 'strict-transport-security': 'max-age=86400; includeSubDomains', 'Vary': 'Accept-Encoding, Accept-Language, Cookie', 'x-content-type-options': 'nosniff', 'X-Frame-Options': 'SAMEORIGIN', 'x-xss-protection': '1; mode=block', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Server': 'cloudflare', 'CF-RAY': '47592380fe671ffa-DFW', 'Content-Encoding': 'gzip'}

print(response.headers['Date']) # Al ser la respuesta de los headers un diccionario, podemos acceder a su información particular

# Tue, 06 Nov 2018 17:04:21 GMT

print(response.text) # Nos devuelve el contenido html del sitio
```