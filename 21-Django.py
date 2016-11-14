
# coding: utf-8

# # Django - Web framework
# ## INSTALLATION
# Using pip: pip install Django

# In[ ]:

# Check if importable
# Should work in Python2 or Python3
# Note - The tutorial actually assumes Python3...
import django
print(django.get_version())


# ## Project Creation
# 
# From terminal:
# *django-admin startproject stat590f*
# 
# Do not name according to common python components
# So things like "test" are a bad name

# ## Security warning
# Don't put your python code in your web server root
# Users might be able to view it...
# You can keep your code anywhere on the server, like the home directory

# ## Description
# 
# The outer root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
# 
# manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
# 
# The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
# 
# mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. (Read more about packages in the official Python docs if you’re a Python beginner.)
# 
# mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
# 
# mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
# 
# mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

# ## Further Steps
# 
# **cd stat590f**
# 
# Edit **stat590f/settings.py**
#     * Change settings as desired
#     * Timezone in particular
#     * Database can be switched to MySQL
#     

# Run **python manage.py migrate**

# Run **python manage.py runserver**

# Browse to **http://127.0.0.1:8000/**

# ## Building First App
# 
# Run **python manage.py startapp polls**
# 
# The first step in writing a database Web app in Django is to define your models – essentially, your database layout, with additional metadata.
# 
# ## Philosophy
# 
# A model is the single, definitive source of truth about your data. It contains the essential fields and behaviors of the data you’re storing. Django follows the DRY Principle. The goal is to define your data model in one place and automatically derive things from it.
# 
# This includes the migrations - unlike in Ruby On Rails, for example, migrations are entirely derived from your models file, and are essentially just a history that Django can roll through to update your database schema to match your current models.
# 
# In our simple poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.
# 
# These concepts are represented by simple Python classes. Edit the polls/models.py file so it looks like this:

# In[ ]:

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# Edit the **stat590f/settings.py** file again, and change the INSTALLED_APPS setting to include the string 'polls'.

# Run **python manage.py makemigrations polls**

# Run **python manage.py migrate**

# Note the three steps to making changes to a model:
# 
# 1. Change your models (in models.py).
# 2. Run python manage.py makemigrations to create migrations for those changes
# 3. Run python manage.py migrate to apply those changes to the database.

# ## Enable Admin User
# 
# 1. Run **python manage.py createsuperuser**
# 2. Edit polls/admin.py to be the following:

# In[ ]:

from django.contrib import admin

from .models import Choice, Question

admin.site.register(Question)
admin.site.register(Choice)


# In[ ]:



