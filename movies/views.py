from django.shortcuts import render,redirect
from .models import *
from user.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def movies(request, profilIsim, profilid):
    profil = Profile.objects.filter(slug = profilIsim).get(id = profilid)
    # filmler = Movie.objects.all()
    populer = Movie.objects.filter(kategori__isim = "Popüler")
    gundemde = Movie.objects.filter(kategori__isim = "Gündemde")
    profiller = Profile.objects.filter(olusturan = request.user)
    context = {
        # 'filmler':filmler
        'populer': populer,
        'gundem': gundemde,
        'profil': profil,
        'profiller':profiller
    }
    return render(request, 'browse-index.html',context)


def view_404(request, exception):
    return redirect('/')

def video(request, filmId):
    film = Movie.objects.get(id = filmId)
    context = {
        'film':film
    }

    return render(request, 'video.html',context)