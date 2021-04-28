# Prueba técnica Enviame

## Pasos previos
Tener instalado docker y docker-compose
Hacer clone del repositorio en algún directorio local.

## Ejercicio 1: Docker
Contenedor 1: Mysql 5.7
Contenedor 2: Restful api con flask

Posicionarse en el directorio y ejecutar el siguiente comando:
> docker-compose up --build

Se montará en localhost:5000 la API y en localhost:3306 la BD

## Ejercicio 2: API CRUD

- GET:http://localhost:5000/api/v1/empresa
- GET:http://localhost:5000/api/v1/empresa/<id>
- POST:http://localhost:5000/api/v1/empresa 
- PUT:http://localhost:5000/api/v1/empresa/<id>
- DEL:http://localhost:5000/api/v1/empresa/<id>

```
Ejemplo cuerpo JSON PUT, POST
{
    "nombre":"microsoft",
    "descripcion":"empresa de software"
}
```
## Ejercicio 3: Análisis + Desarrollo
## Ejercicio 4: Consumo API Envíame para la creación de un envío
## Ejercicio 5: Análisis + Desarrollo

Revisar o ejecutar archivo:
> cant_divisores_fibonacci.py

## Ejercicio 6: Análisis + Desarrollo Aplicado a Negocio
## Ejercicio 7: SQL
Query
```
UPDATE employees e
   SET e.salary = e.salary + e.salary*(SELECT ct.anual_adjustment/100
						 	             FROM continents ct,
						 					  countries c
										WHERE ct.id = c.continent_id
						  			  	  AND c.id = e.country_id)
 WHERE e.salary <= 5000
```
