
### Configuración Apache
Editar el archivo de configuración:
```
nano /etc/apache2/sites-available/000-default.conf
```

Agregar los siguientes ajustes:
```
ServerName www.atencionpresencial-sena.grupoasd.com
ServerAlias atencionpresencial-sena.grupoasd.com
DocumentRoot /var/www/html/proyecto/DevSena/sena

Alias /static/ /var/www/html/proyecto/DevSena/sena/static/
<Directory /var/www/html/proyecto/DevSena/sena/static>
    Require all granted
</Directory>
<Directory /var/www/html/proyecto/DevSena/sena>
    Require all granted
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>
WSGIDaemonProcess atencionpresencial-sena.grupoasd.com python-path=/var/www/html/proyecto/DevSena python-home=/var/www/html/proyecto/env2
WSGIProcessGroup atencionpresencial-sena.grupoasd.com
WSGIPassAuthorization on
WSGIScriptAlias / /var/www/html/proyecto/DevSena/sena/sena/wsgi.py
```