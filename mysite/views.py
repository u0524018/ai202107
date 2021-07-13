from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from mysite.models import Post

def index(request):
	name = "林桐生"
	special = random.randint(1, 42)
	lotto = [random.randint(1, 42) for i in range(6)]
	return render(request, "index.html", locals())


def news(request):
	posts = Post.objects.all()
	return render(request, "news.html", locals())

def show(request, id):
	try:
		post = Post.objects.get(id=id)
	except:
		return redirect("/news/")
	return render(request, "show.html", locals())