from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.

def mform(request):
	af = ArticleForm()
	article_Objs = Article.objects.all()


	if request.method == "POST":
	   afNew = ArticleForm(request.POST)
	   afNew.save()
	   return redirect('/app3/mform')

	return render(request, "add_article.html", {'obj': af, 'aobjs': article_Objs})

def delete_article():
    aObj = Article.objects.get(id=id)
    aObj.delete()
    return redirect ('/app3/mform/')

def update_article():
	pass
