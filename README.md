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