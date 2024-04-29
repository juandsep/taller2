# Taller2-G8-Valencia-Sepulveda-Rueda-Dussan-Vargas
# Documentación del Sistema de Recomendación Basado en el Filtro Colaborativo

## Descripción General

Este sistema de recomendación se basa en el enfoque de filtrado colaborativo. Utiliza las interacciones pasadas de los usuarios con los elementos para predecir qué otros elementos podrían interesarles.

## Preparación de los Datos

Los datos utilizados en este sistema provienen de varios archivos JSON grandes. Cada archivo contiene diferentes tipos de datos:

- `review.json`: Contiene las reseñas de los usuarios para diferentes negocios.
- `business.json`: Contiene información sobre los negocios.
- `user.json`: Contiene información sobre los usuarios.

Para manejar el tamaño de estos archivos, se implementó un proceso para leer los archivos en fragmentos de 500 filas a la vez. Cada fragmento se guarda en un DataFrame de pandas separado para su posterior procesamiento.

## Implementación del Modelo

El modelo de filtrado colaborativo se implementa utilizando la biblioteca Surprise de Python, que proporciona varias herramientas para construir y analizar sistemas de recomendación.

## Evaluación del Modelo

El rendimiento del modelo se evalúa utilizando una métrica de error cuadrático medio (RMSE). Se realiza una validación cruzada para obtener una estimación más robusta del rendimiento del modelo.