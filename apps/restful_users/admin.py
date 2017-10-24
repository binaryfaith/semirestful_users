from __future__ import absolute_import
from django.contrib import admin
from django import forms

from . models import User

admin.site.register(User)
