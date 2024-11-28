# Ofir assignment


First bootstrap the development environment

```bash

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt


```

Next you'l need to initialize the database
and import some data into it.

You can use the [just](https://github.com/casey/just) tool and it's an oneliner!.

_If you use just, the superuser user name will be `admin` and the password will be `password`._

```bash
# This will run migrations, import  data 
# and setup a super user
just bootstrap
```

The manuel way:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # If you want access to the admin interface
python manage.py import
```

And finally start the server

```bash
python manage.py runserver
```


