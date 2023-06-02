from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PhoneSales(models.Model):
    author=models.ForeignKey(User,on_delete = models.CASCADE,verbose_name="İlan Sahibi",related_name="PhoneSales")
    is_active = models.BooleanField(verbose_name="İlan Aktif mi?",default=False)
    label=models.CharField(max_length=50,null=True,blank=False,default="Telefon-Satış",verbose_name="Etiket(Telefon Satış)")
    phone_brand=models.CharField(max_length=250,null=True,blank=False,verbose_name="Telefon Markası")
    phone_model=models.CharField(max_length=250,null=True,blank=False,verbose_name="Telefon Modeli")
    os=models.CharField(max_length=8,null=True,blank=False,verbose_name="Telefon İşletim Sistemi",default="Android")
    ram_memory=models.CharField(max_length=6,null=True,blank=False,verbose_name="Telefon Ram Bellek")
    memory_memory=models.CharField(max_length=6,null=True,blank=False,verbose_name="Telefon Hafıza Bellek")
    situation=models.CharField(max_length=10,null=True,blank=False,verbose_name="Telefon Durumu",default="İkinci El")
    garanti=models.CharField(max_length=21,null=True,blank=False,verbose_name="Garanti",default="Garantisi Yok")
    swap=models.CharField(max_length=6,null=True,blank=False,verbose_name="Takas Durumu")
    city=models.CharField(max_length=100,null=True,blank=False,verbose_name="İl")
    district=models.CharField(max_length=100,null=True,blank=False,verbose_name=" İlçe")
    price=models.DecimalField(max_digits=10,null=True,blank=False, decimal_places=3)
    comment=models.TextField(null=True,blank=False,verbose_name="Açıklama")
    avatar = models.FileField(upload_to='PhoneSales/', blank=False,null=True,verbose_name="İlan Resmi")

    created_date=models.DateTimeField(auto_now=True,verbose_name="Oluşturulma Tarihi")

    def author_id(self):
        return self.author,self.avatar
    
    def __str__(self):
        return  'author={0}, is_active={1}'.format(self.author, self.is_active)



class MobileRepair(models.Model):
    author=models.ForeignKey(User,on_delete = models.CASCADE,verbose_name="İlan Sahibi",related_name="MobileRepair")
    is_active = models.BooleanField(verbose_name="İlan Aktif mi?",default=False)
    jobfinish= models.BooleanField(verbose_name="Ürün Teslim Edildi Mi?",default=False)
    acceptance= models.BooleanField(verbose_name="İstek Onaylı Mı?",default=False)
    label=models.CharField(max_length=50,null=True,blank=False,default="Telefon-Tamir",verbose_name="Etiket(Telefon-Tamir)")
    phone_brand=models.CharField(max_length=250,null=True,blank=False,verbose_name="Telefon Markası")
    phone_model=models.CharField(max_length=250,null=True,blank=False,verbose_name="Telefon Modeli")
    city=models.CharField(max_length=100,null=True,blank=False,verbose_name="İl")
    district=models.CharField(max_length=100,null=True,blank=False,verbose_name=" İlçe")
    avatar = models.FileField(upload_to='MobileRepair/', blank=False,null=True,verbose_name="Tamir Resmi")
    comment=models.TextField(null=True,blank=False,verbose_name="Açıklama")
    created_date=models.DateTimeField(auto_now=True,verbose_name="Oluşturulma Tarihi")

    def author_id(self):
        return self.author,self.avatar
    
    def __str__(self):
        return  'Marka={0}, Model={1}'.format(self.phone_brand, self.phone_model)



class PhonePart(models.Model):
    author=models.ForeignKey(User,on_delete = models.CASCADE,verbose_name="İlan Sahibi",related_name="PhonePart")
    is_active = models.BooleanField(verbose_name="İlan Aktif mi?",default=False)
    label=models.CharField(max_length=50,null=True,blank=False,default="Telefon-Parçası",verbose_name="Etiket(Telefon-Parçası)")
    part_name=models.CharField(max_length=110,null=True,blank=False,verbose_name="Telefon-Parçası")
    situation=models.CharField(max_length=10,null=True,blank=False,verbose_name="Telefon Durumu",default="İkinci El")
    garanti=models.CharField(max_length=21,null=True,blank=False,verbose_name="Garanti",default="Garantisi Yok")
    swap=models.CharField(max_length=6,null=True,blank=False,verbose_name="Takas Durumu")
    city=models.CharField(max_length=100,null=True,blank=False,verbose_name="İl")
    district=models.CharField(max_length=100,null=True,blank=False,verbose_name=" İlçe")
    price=models.DecimalField(max_digits=10,null=True,blank=False, decimal_places=3)
    
    avatar = models.FileField(upload_to='PhonePart/', blank=False,null=True,verbose_name="Tamir Resmi")
    comment=models.TextField(null=True,blank=False,verbose_name="Açıklama")
    created_date=models.DateTimeField(auto_now=True,verbose_name="Oluşturulma Tarihi")

    def author_id(self):
        return self.author,self.avatar
    
    def __str__(self):
        return  'author={0}, is_active={1}'.format(self.author, self.is_active)





class PhoneAksesuar(models.Model):
    author=models.ForeignKey(User,on_delete = models.CASCADE,verbose_name="İlan Sahibi",related_name="PhoneAksesuar")
    is_active = models.BooleanField(verbose_name="İlan Aktif mi?",default=False)
    label=models.CharField(max_length=50,null=True,blank=False,default="Telefon-Aksesuar",verbose_name="Telefon-Aksesuarı")
    aksesuar_name=models.CharField(max_length=110,null=True,blank=False,verbose_name="Aksesuar Adı")
    situation=models.CharField(max_length=10,null=True,blank=False,verbose_name="Aksesuar Durumu",default="İkinci El")
    city=models.CharField(max_length=100,null=True,blank=False,verbose_name="İl")
    district=models.CharField(max_length=100,null=True,blank=False,verbose_name=" İlçe")
    price=models.DecimalField(max_digits=10,null=True,blank=False, decimal_places=3)
    comment=models.TextField(null=True,blank=False,verbose_name="Açıklama")
    avatar = models.FileField(upload_to='PhoneAksesuar/', blank=False,null=True,verbose_name="İlan Resmi")
    created_date=models.DateTimeField(auto_now=True,verbose_name="Oluşturulma Tarihi")

    def author_id(self):
        return self.author,self.avatar
    
    def __str__(self):
        return  'author={0}, is_active={1}'.format(self.author, self.is_active)

