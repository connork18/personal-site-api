# personal-site-api
The django-rest-framework api for my personal site, connorkelley.in

```
pyenv activate blog-venv-2
python manage.py runserver
```

# activate venv on the aws eb server #

```
source /var/app/venv/*/bin/activate
export $(sudo cat /opt/elasticbeanstalk/deployment/env | xargs)
cd /var/app/current
```

```
python manage.py shell
from blog.models import Post
Post.objects.all().delete()
from blog.temp.post_migrator import migrate_posts
migrate_posts()
```

# Deploy to elastic beanstalk
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-configure-for-eb

Note--make sure you commit changes to git repo before deploying

# Database
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html

# Create admin superuser
