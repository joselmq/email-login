# email-login

```buildoutcfg
virtualenv -p /usr/local/bin/python3.8 ~/.virtualenvs/example_project-3.8
source ~/.virtualenvs/example_project-3.8/bin/activate

sudo -u postgres createuser --interactive
jose
y
sudo -u postgres createdb jose
sudo -u jose psql
ALTER USER jose PASSWORD '123456';

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

127.0.0.1:8000/admin
127.0.0.1:8000/api/accounts/signup
```