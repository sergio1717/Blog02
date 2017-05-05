# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from Blog02.models import Category, Post, Comment
import datetime




list_category = Category.objects.all()
fecha_actual = datetime.datetime.now()



# Create your views here.
def welcome(request):
	
	return render(request, 'welcome.html', {'list_category': list_category,'fecha_actual': fecha_actual})


def post(request):
	
	list_post = Post.objects.all()

	return render(request, 'post_filter.html',{'list_post': list_post, 'list_category': list_category,'fecha_actual': fecha_actual})


def posts_by_filter(request, offset):
	try: 
		offset = str(offset) 
	except ValueError: 
		raise Http404()  
	list_post = Post.objects.filter(category__name = offset)

	return render(request, "post_filter.html",{'list_post':list_post, 'list_category':list_category,'fecha_actual': fecha_actual})


def comment_by_post(request, offset):
	try: 
		offset = str(offset) 
	except ValueError: 
		raise Http404()  
	list_comment = Comment.objects.all()#filter(post__title = offset)      #comentado porque no hay conincidencias entre el titulo del post 

	return render(request, "comment_filter.html",{'list_comment':list_comment, 'list_category':list_category,'fecha_actual': fecha_actual})