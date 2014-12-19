Android_API_REST
================

API REST creada para una app en android..

se Utiliza Django como backend y para proporcionar nuestra API REST

Para usar esta app debes tener instalado pythony pip inicialmente.

habrimos una consola y ejecutamos el siguiente comando de pip para instalar los paquetes requeridos

(si en Windows no te reconoce el comando pip es pq debes agregarlo al la variable de entorno o bien puedes ir al directorio del binario que es en el directorio de instalacion de python carpeta /Scripts)
$ pip install -r requirements.txt (Es necesario conexion a internet)

Una vez concluido la instalacion solo debemos poner a ejecutar el servidor

$ python manage.py runserver 0.0.0.0:8000 (el puerto puede ser cualquiera q este libre)

una vez arrancado accedemos al la api

```
localhost/api
localhost/admin
```
el usuario del admin es edx clave edx
si quieres reiniciar la bd borras el db.sqlite3 y ejecutas
$ python manage.py syncdb


