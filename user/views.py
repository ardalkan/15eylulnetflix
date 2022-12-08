from django.shortcuts import render,redirect
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .models import *
# Create your views here.
def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre = request.POST['sifre']
        sifre2 = request.POST.get('sifre2')
        resim = request.FILES['resim']
        tel = request.POST['telefon']

        if sifre == sifre2:
            if User.objects.filter(username = kullanici).exists():
                messages.error(request, 'Bu kullanıcı adı zaten mevcut')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Bu email zaten kullanımda')
                return redirect('register')
            elif len(sifre)<6:
                messages.error(request, 'Şifre en az 6 karakter olması gerekiyor')
                return redirect('register')
            elif kullanici.lower() in sifre:
                messages.error(request, 'Şifre ile kullanıcı adı benzer olmamalıdır')
                return redirect('register')
            else:
                user = User.objects.create_user(username=kullanici, email=email, password=sifre)
                Hesap.objects.create(user= user, resim = resim, tel =tel )
                user.save()
                messages.success(request, 'Kullanıcı oluşturuldu')
                return redirect('index')
        else:
            messages.warning(request, 'Şifreler uyuşmuyor')
            return redirect('register')
    return render(request, 'register.html')

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username=kullanici, password=sifre)
        if user is not None:
            login(request,user)
            messages.success(request,'Giriş yapıldı.')
            return redirect('profiles')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
    return render(request, 'login.html')

def profiles(request):
    profiller = Profile.objects.filter(olusturan = request.user)
    context = {
        'profiller':profiller
    }
    return render(request, 'browse.html',context)

def create(request):
    form = ProfileForm()
    if request.method == 'POST':
        try:
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                if Profile.objects.filter(olusturan = request.user).count() < 4:
                    profil = form.save(commit=False)
                    profil.olusturan = request.user
                    profil.save()
                    messages.success(request,'Proil oluşturuldu')
                    return redirect('profiles')
                else:
                    messages.error(request,'En fazla 4 adet proil olabilir')
                    return redirect('profiles')
        except:
            messages.error(request,  'Bilinmeyen bir hata oluştu lütfen tekrar deneyiniz. Düzelmediği takdirde bizimle iletişime geçebilirsiniz.')
            return redirect('create')

    context = {
        'form' : form
    }
    return render(request, "create.html", context)

def hesap(request):
    profil = request.user.hesap

    context = {
        'profil':profil
    }
    return render(request,'hesap.html',context)


def update(request):
    form = UserForm(instance = request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bilgiler Güncellendi')
            return redirect('hesap')

    context = {
        'form':form
    }
    return render(request, 'update.html', context)

def reset(request):
    if request.method == "POST":
        eski = request.POST['eski']
        yeni1 = request.POST['yeni1']
        yeni2 = request.POST['yeni2']

        user = authenticate(request, username = request.user, password = eski)
        if user is not None:
            if yeni1 == yeni2:
                kullanici = request.user
                kullanici.set_password(yeni1)
                kullanici.save()
                messages.success(request, 'Şifre başarıyla değiştirildi. Tekrardan giriş yapınız')
                return redirect('login')
            else:
                messages.error(request,'Şifreler uyuşmuyor')
                return redirect('reset')
        else:
            messages.error(request, 'Şİfreler uyuşmuyor')
            return redirect('reset')
    return render(request,'resetPassword.html')


# hesap silme
def userDelete(request):
    user = request.user
    user.delete()
    messages.success(request,'Hesap başarıyla silindi.')
    return redirect('index')

