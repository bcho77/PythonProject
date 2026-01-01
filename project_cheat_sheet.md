# Django Project Cheatsheet (DevOps & Backend)

## Project & App Management

```bash
django-admin startproject myproject   # Create project
cd myproject
python manage.py startapp myapp       # Create app
python manage.py check                # Check project for issues
```

## Development Server

```bash
python manage.py runserver            # Run dev server
python manage.py runserver 0.0.0.0:8000
```

## Settings & Configuration

```bash
python manage.py diffsettings         # Compare default vs custom settings
python manage.py check --deploy       # Production readiness check
```

## Database & Migrations

```bash
python manage.py makemigrations       # Create migrations
python manage.py migrate              # Apply migrations
python manage.py showmigrations       # List migrations
python manage.py sqlmigrate app 0001  # Show SQL for migration
```

## Django Models & Shell

```bash
python manage.py shell                # Django shell
python manage.py dbshell              # Database shell
```

## Superuser & Auth

```bash
python manage.py createsuperuser      # Create admin user
python manage.py changepassword user  # Change password
```

## Static & Media Files

```bash
python manage.py collectstatic        # Collect static files
python manage.py findstatic admin.css # Locate static file
```

## Templates

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

## URLs & Views

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

## Admin

```python
from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
```

## Testing

```bash
python manage.py test                 # Run tests
python manage.py test myapp           # Test specific app
```

## Fixtures & Data

```bash
python manage.py dumpdata app.Model > data.json
python manage.py loaddata data.json
```

## Internationalization (i18n)

```bash
python manage.py makemessages -l fr
python manage.py compilemessages
```

## Caching

```bash
python manage.py createcachetable
```

## Debugging & Logs

```bash
python manage.py shell_plus           # django-extensions
python manage.py runserver --verbosity 3
```

## Security & Production

```bash
pip install gunicorn
pip install whitenoise
python manage.py check --deploy
```

## Common Django Errors

* Missing `{% load static %}` in templates
* Migrations not applied
* DEBUG=True in production
* Static files not collected

## Typical Django Workflow

```bash
python -m venv venv
source venv/bin/activate
pip install django
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt


django-admin startproject project
python manage.py migrate
python manage.py runserver

pip install python-decouple

```

---

*This Django cheatsheet covers the most common commands, patterns, and best practices for Django development and DevOps deployment.*
