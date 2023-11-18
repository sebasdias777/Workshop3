# Workshop3
Este Workshop se centra en realizar transformaciones relevantes en cinco archivos CSV correspondientes a diferentes años (2015, 2016, 2017, 2018, 2019). El objetivo principal es aplicar un modelo de regresión lineal en Python para predecir la columna "Happiness Score" basándose en los datos históricos de estos archivos CSV. Posteriormente, se guarda la predicción obtenida junto con los datos originales en una base de datos PostgreSQL.

## Tecnologías Utilizadas
Docker: Para la gestión y despliegue del entorno de desarrollo.

Python: Lenguaje de programación principal utilizado en el proyecto.

Joblib: Para guardar y cargar modelos de Python.

Jupyter Notebook: Utilizado para el desarrollo interactivo y documentación.

Kafka: Posible uso para la transmisión de datos en tiempo real.

Scikit-Learn: Biblioteca de aprendizaje automático utilizada para la implementación del modelo de regresión lineal.

PostgreSQL: Sistema de gestión de bases de datos relacional utilizado para almacenar los datos originales y las predicciones.

## Pasos Realizados
Transformación de los Archivos CSV: Los archivos CSV correspondientes a los años 2015 a 2019 fueron sometidos a procesos de limpieza, preprocesamiento y transformación para su utilización en el modelo de regresión.

Selección y Entrenamiento del Modelo de Regresión Lineal: Utilizando Scikit-Learn en Python, se implementó un modelo de regresión lineal para predecir el "Happiness Score" basado en los datos transformados.

Guardado de la Predicción en PostgreSQL: Una vez obtenida la predicción, se combinó con los datos originales y se almacenó en una base de datos PostgreSQL para su posterior análisis y referencia.

## Instrucciones de Ejecución

Clona este repositorio a tu entorno local.

``` Git clone https://github.com/sebasdias777/Workshop3 ```

Asegúrate de tener Docker instalado y ejecuta el entorno con los archivos proporcionados.

``` docker compose up -d  ```

Entramos al contenedor de kafka , y poteriormnete creamos el topic.

``` docker exec -it kafka-test bash ```

``` kafka-topics --bootstrap-server kafka-test:9092 --create --topic Workshop3 ```

Se ejecuta los mains de producer.py y consumer.py 

``` python3 main_consumer.py  ```

``` python3 main.py ```
