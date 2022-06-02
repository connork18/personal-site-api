# personal-site-api
The django-rest-framework api for my personal site, connorkelley.in

```
pyenv activate blog-venv
python manage.py runserver
```

# DELETE THEN MIGRATE ALL EXISTING POSTS #

```
from blog.models import Post
Post.objects.all().delete()
```

# Deploy to elastic beanstalk
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-configure-for-eb

# Database
I wanted to just use my db.sqlite3 database. I ran into some issues though that I admittedly didn't put much effort towards overcoming. So I added a postgres database with AWS RDS.

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html