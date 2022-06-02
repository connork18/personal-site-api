---
title: 'Building this API: Data models (2/n)'
date: '2022-01-18'
---

### Quick Personal Note ###
It was a long day, my daughter has been sick and was coughing all night last night and none of us got much sleep. Writing some code that will eventually help me start tracking my workouts, what I'm reading, and other stuff on my website will be a nice and therapeutic before going to bed.

### Actual dev stuff ###
Alright, digging back in. Gonna confirm all is good. 

pyenv activate blog-venv  
python manage.py runserver  

<Image
priority
src="/images/django-screenshot.png"
height={144}
alt={name}
/>

Right, I wired up those /users and /groups endpoints.

Okay, the data model my front-end uses is:

slug: string;  
title: string;  
date: <strong>string;</strong> ... I am going to change this to an actual datetime   
contentHtml: string;  

I referenced another <a href="https://djangocentral.com/building-a-blog-application-with-django/">blog tutorial</a> to see if I am missing anything. I am going to go with the following:

 * title = models.CharField(max_length=200, unique=True)  
 * slug = models.SlugField(max_length=200, unique=True)  
 * updated_on = models.DateTimeField(auto_now=True)  
 * content = models.TextField()  
 * created_on = models.DateTimeField(auto_now_add=True)  
 * status = models.IntegerField(choices=STATUS, default=0)  
   * STATUS = ((0, "Draft"),(1, "Publish"))  

Okay so my blog.models is updated. I need to add 'blog' to my INSTALLED_APPS in the settings module. And make the migrations to my db.

python manage.py makemigrations  
python manage.py migrate  

I am going to quickly install httpie to easily test the api instead of using curl or the browser

pip install httpie  

Okay, so now I need to create my serializer--it will be a ModelSerializer to save me the pain of rewriting the datatypes for each field and stuff. I am going to use a ReadOnlyModelViewSet for the API since clients (other than my admin app) will only be able to read the published posts. Once I write those and wire up the urls, I am good to go. 

Note to self: this is easily referenceable jumping around in the django-rest-framework <a href="https://www.django-rest-framework.org/tutorial/1-serialization/">tutorial</a> and the <a href="https://www.django-rest-framework.org/api-guide/viewsets/#readonlymodelviewset">API guide</a>.

Everything is working well, but I have no blog posts!

I would like to use my admin app to create posts. I kind of forget off the top of my head how that works, but know I need to add some stuff to the admin.py module. 

<a href="https://docs.djangoproject.com/en/4.0/intro/tutorial07/">Here</a> is a good link. I also referenced the options they used in <a href="https://docs.djangoproject.com/en/4.0/intro/tutorial07/">this tutorial</a> to take a shortcut to some things I would probably want.

I was able to publish my first post in my local DB. Cool!

<Image
priority
src="/images/django-screenshot1.png"
height={144}
alt={name}
/>

Before pushing to github, I am going to use <a href="https://github.com/github/gitignore/blob/main/Python.gitignore">a boilerplate gitignore</a>.

There are a few changes I might want to make for convenience, but I think next I want to write a migrator that will help me dump all of my existing blog posts into local database entries to backfill the writing that I have done so far.

That took me an hour--not a lot of work in an hour, but I am writing, had some debugging and docs perusing to refresh my memory.









