from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify
# Create your models here.
class Profile(models.Model):
    olusturan = models.ForeignKey(User,related_name='olusturan' ,on_delete=models.CASCADE)
    isim = models.CharField(max_length=100)
    resim = models.FileField(upload_to="profiles/", verbose_name="Profil resmi")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(null=True, blank=True,editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super(Profile, self).save(*args,**kwargs)

    def __str__(self):
        return self.isim

class Hesap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resim = models.FileField(upload_to="hesaplar/")
    tel = models.IntegerField()

    def __str__(self): 
        return self.user.username # hangi bilgi gösterilecek