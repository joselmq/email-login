# email-login

App que permite el logueo vía e-mail, permite agregar usuarios, pero estoy estancado en la activación vía email.
```buildoutcfg
SMTPAuthenticationError at /api/accounts/signup/

(535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials s18sm2978529qkj.87 - gsmtp')
```

* Cree un correo al que le activé 'Contraseñas de aplicaciones' y habilité otras opciones también.
* El usuario registrado es almacenado en la ddbb con 'is_active=False'

 
Comandos:

```buildoutcfg
virtualenv -p /usr/local/bin/python3.8 ~/.virtualenvs/example_project-3.8
source ~/.virtualenvs/example_project-3.8/bin/activate

sudo -u postgres createuser --interactive
jose
y
sudo -u postgres createdb jose
sudo -u jose psql
ALTER USER jose PASSWORD '123456';

cd loginApp
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

127.0.0.1:8000/admin
127.0.0.1:8000/api/accounts/signup
```

requirements.txt está en 'example_project/axample_project/requirements.txt'