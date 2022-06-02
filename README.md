# personal-site-api
The django-rest-framework api for my personal site, connorkelley.in

```
pyenv activate blog-venv
python manage.py runserver
```

# activate venv on the aws eb server #

```
source /var/app/venv/*/bin/activate
cd /var/app/current
```

```
python manage.py shell
from blog.temp.post_migrator import migrate_posts
migrate_posts()
```

# Deploy to elastic beanstalk
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-configure-for-eb

# Note--make sure you commit changes to git repo before deploying

# Database
I wanted to just use my db.sqlite3 database. I ran into some issues though that I admittedly didn't put much effort towards overcoming. So I added a postgres database with AWS RDS.

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html