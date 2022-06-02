---
title: 'Building this API: Project set up (1/n)'
date: '2022-01-16'
---

Currently, this website is completely static and isn't fetching any data from a database.

I built it using Next.js, a next-generation React.js framework. And all the blog posts are stored locally in the same directory as my website code. The code was deployed on Vercel, a hosting provider that is crazy easy.

There are basically two main pieces:

 * The computer Vercel is using to run and host my Next.js website
 * The browser you are using to fetch, render and interact with my website

I would like to introduce two more parties:

 * Another computer where I can host a Python API
 * A database that stores data for my posts and other things I build

Then, my blog would be built with a "Django + React" stack -- a common enough SaaS stack.

The biggest app I have built has been with a Django + React <strong>Native</strong> stack. I have been pretty surprised at the differences between mobile and web development, despite using <i>almost</i> the exact same framework. 

Goals:
 1. I want a space on the internet that I can continue to experiment in and develop
 2. I want to build more familiarity with spinning up SaaS products quickly

I am documenting my project set up because I HATE project set up. I haven't built a bazillion apps, I have just worked really hard on a few. So the act of building something new is daunting and annoying. I would like it to be something I can do in my sleep. Maybe writing it all down will help.


## Project set up ##
Going to use Python 3.9 and manage my virtualenv with pyenv. This is my favorite article that I come back to when I forget the syntax, etc: https://realpython.com/intro-to-pyenv/

The latest bugfix release of Python 3.9 available via pyenv is 3.9.6. I am a dummy and don't know why I wouldn't use version 3.9.6 over 3.9.0 if 3.9.6 has fixed some bugs that were in the initial 3.9.0 release. So that's what I did -- I imagine it will not make a bit of difference for me since I am not doing complex stuff.

pyenv install 3.9.6  

Although I realize that I am just wasting precious time by waiting for it to install... I should have just gone with 3.8.11, my latest version of python which is not being deprecated for a long time. C'est la vie. I am going to make some tea.

Okay, now I'm creating my virtualenv:

pyenv virtualenv 3.9.6 blog-venv  
pyenv activate blog-venv

Now, install Django 4.0.1

python -m pip install Django

Now I am going to my ~/ directory in the terminal and starting my django project.

django-admin startproject mysite  
cd mysite  
python manage.py runserver  

All is working correctly. Running the server looks like it might have auto-created my local sqlite3 for me. 

Now I am following the set up instructions on django-rest-framework.com.

pip install djangorestframework  
pip install markdown  
pip install django-filter  

Okay, before I get going, I am going to initialize as a github repository so I can use git to document my progress and development. <a href="https://docs.github.com/en/github/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line">This</a> is the link I used to refresh my memory on doing my initial commit from the command line.

This is going to be one of my first open source repositories. I want to make sure I keep my secrets, etc secure, although I am not going to deploy it to production soon. 

I am going to rename my django project's directory to "personal-site-api" before I do that.

mv ~/mysite ~/personal-site-api

Andddd I want to set up my .gitignore file and requirements.txt file.

touch .gitignore

Edited the file --> *.sqlite3

pip freeze > requirements.txt

git init -b main
git add . && git commit -m "initial commit"  

I'm just going to create the repo manually on GitHub rather than downloading the github cli. I haven't used it before and am comfortable just using git for my pull requests and stuff.

Ugh, I added a readme.md so now my initial commit is all wonky. I had to 'git pull --allow-unrelated-histories [repo git url]' to get everything back to normal.

On to django stuff-- I am going to set up my admin user so I can access the admin portal which I will eventually use to create blog posts.

python manage.py migrate
python manage.py createsuperuser
django-admin startapp blog

Now, I am going to run through the quickstart docs to help get refreshed with django-rest-framework fast: https://www.django-rest-framework.org/tutorial/quickstart/.

All is working well. Now I need to create my blog post model. I am going to try to keep it relatively aligned with how my blog posts are being broken down on my front-end right now. They are written as consistently-formatted markdown files and then parsed into:

slug: string;  
title: string;  
date: <strong>string;</strong> ... I am going to change this to an actual datetime   
contentHtml: string;  

I haven't created a model that was intended to be rendered as HTML before. I think it can just be a 

I'll pick up the model creation next post. This one is getting long.
















