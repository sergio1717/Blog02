# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Blog02.models import Post, Comment, Category	#importamos las clases creadas en blog

admin.autodiscover()

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)