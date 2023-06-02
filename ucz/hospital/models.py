from django.db import models
from django.contrib.auth.models import User
from advert .models import MobileRepair

# Create your models here.
class PhoneRepairRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_request' ,verbose_name="İsteği Atan")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_request',verbose_name="İsteği Alan")
    acceptance= models.BooleanField(verbose_name="İstek Onaylı Mı?",default=False)
    jobfinish= models.BooleanField(verbose_name="Ürün Teslim Edildi Mi? Telefon Sahibi Onay",default=False)
    jobfinish_business= models.BooleanField(verbose_name="Ürün Teslim Edildi Mi? İşletme Sahibi Onay",default=False)
    product= models.IntegerField(null=True,verbose_name="Hangi İlan")
    city=models.CharField(max_length=100,null=True,blank=False,verbose_name="İl")
    district=models.CharField(max_length=100,null=True,blank=False,verbose_name=" İlçe")
    phone_brand=models.CharField(max_length=250,null=True,blank=False,verbose_name="Telefon Markası")
    phone_model=models.CharField(max_length=250,null=True,blank=False,verbose_name="Telefon Modeli")
    created_date=models.DateTimeField(auto_now=True,verbose_name="Oluşturulma Tarihi")
#   jobfinish_created_date=models.DateTimeField(auto_now=False,verbose_name="Teslim Tarihi")

    def __str__(self):
        return  'sender={0}, acceptance={1}'.format(self.sender, self.acceptance)