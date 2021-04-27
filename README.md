### Ejercicio 1: Docker

Contenedor 1: Mysql 5.7
Contenedor 2: Restful api con flask

Tener instalado docker y docker-compose

Bajar el repositorio en algún directorio, ejecutar el siguiente comando:

'docker-compose up --build'

Se montará en localhost:5000 la API y en localhost:3306 la BD

### Ejercicio 2: API CRUD

-- GET:http://localhost:5000/api/v1/empresa
-- GET:http://localhost:5000/api/v1/empresa/<id>

-- POST:http://localhost:5000/api/v1/empresa 
'{
    "nombre":"microsoft",
    "descripcion":"empresa de software"
}'

-- PUT:http://localhost:5000/api/v1/empresa/<id>
'{
    "nombre":"microsoft",
    "descripcion":"empresa de software"
}'

-- DEL:http://localhost:5000/api/v1/empresa/<id>
