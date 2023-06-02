from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BusinessStaff(models.Model):
    author=models.ForeignKey(User,on_delete = models.CASCADE,verbose_name="Kullanıcı Adı",related_name="author")
    is_active = models.BooleanField(default=False,verbose_name="Kullanıcı Aktif mi?")
    is_staff = models.BooleanField(default=False,verbose_name="Kullanıcı Dükkan Sahibi mi?")
    office_phone=models.CharField(unique=True,null=True, blank=True,max_length=11,verbose_name='İş Telefonu')
    mobile_phone=models.CharField(unique=True,null=True, blank=False,max_length=11,verbose_name='Cep Telefonu')
    avatar = models.FileField(upload_to='uploads/', blank=False,null=True,)
    #website = models.URLField(max_length = 200, blank=True, null=True,verbose_name="Web Site")
    biography = models.TextField( blank=False, null=True,verbose_name="Biyografi")
    social_media_facebook=models.TextField(null=True, blank=True,verbose_name="Facebook Sosyal Medya")
    social_media_twitter=models.TextField(null=True, blank=True,verbose_name="Twitter Sosyal Medya")
    social_media_instagram=models.TextField(null=True, blank=True,verbose_name="İnstagram Sosyal Medya")
    social_media_tiktok=models.TextField(null=True, blank=True,verbose_name="Tiktok Sosyal Medya")


    views=models.IntegerField(null=True, blank=True,default=0,verbose_name="Görüntülenme Sayısı")
    sharing=models.CharField(max_length=8,null=True,blank=True,verbose_name="İlan Sayısı",default=0)
    city=models.CharField(max_length=100,null=True,blank=False,verbose_name="İl")
    district=models.CharField(max_length=100,null=True,blank=False,verbose_name=" İlçe")
    address=models.TextField(null=True, blank=False,verbose_name="Açık Adres")
    created_date=models.DateTimeField(auto_now=True,verbose_name="Oluşturulma Tarihi")
    #email = models.EmailField(unique=True)

    def author_id(self):
        return self.author
    
    def __str__(self):
        return  'author={0}, is_staff={1}'.format(self.author, self.is_staff)