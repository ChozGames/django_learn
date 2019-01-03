from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime
from blog.models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {"articles": articles})

def lire(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if id_article > 100:
        raise Http404
    elif id_article == 10:
    	return redirect(google)

    return HttpResponse(
    	"Vous avez demandé l'article n° {0} !".format(id_article)
    )

def google(request):
	return redirect("http://google.fr")

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)  
    )

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
