# Ofir assignment


First bootstrap the development environment

```bash

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt


```

Next you'l need to initialize the database
and import some data into it.

You _can_ use the [just](https://github.com/casey/just) tool for that.

_If you use just, the superuser user name will be `admin` and the password will be `password`._

```bash
# This will run migrations, import  data 
# and setup a super user
just bootstrap
```

If you wont or can't use ```just```:

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

Or if you're using just:

```
just bootstrap run
```

## Details

### Technology
I'm using Django restframework for the restful stuff under the `/api/*` urls.
For dynamic updates on the client, I'm using [htmx](https://htmx.org/)
I've also included the django htmx module for easier usage.
Tailwindcss is used for styling.

For scraping data [scrapy](https://scrapy.org/) is used.

### Fixture data
The data is scraped from [ofir.dk](https://ofir.dk)
You can run the scraping script by running ```python -m scrapy runspider ./scripts/spider.py -o fixtures/imports.jsonl``` and then import it with ```python manage.py import```.  
Or if you're feeling fancy, you can use the oneliner: ```just import```.

### Sitemap:

```bash
/ # Jobposting list
/job/:id # Jobposting details
/api/jobs # Restful jobpostings api
/api/categories # Restful categories api
/admin # Admin interface

```
