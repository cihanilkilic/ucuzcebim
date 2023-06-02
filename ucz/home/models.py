from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name_surname=models.CharField(max_length=100,verbose_name="Ad-Soyad",null=True,blank=False)
    mail_address=models.CharField(max_length=50,verbose_name="Mail Adresi",null=True,blank=False)
    telephone=models.CharField(max_length=11,verbose_name="Telefon Numarası",null=True,blank=False)
    message=models.TextField(verbose_name="Mesajı",null=True,blank=False)
    created_date=models.DateTimeField(auto_now=True,verbose_name="Gönderilme Tarihi")

    def __str__(self):
        return  'Ad-Soyad={0}, Mesajı={1}, Gönderilme Tarihi{2}'.format(self.name_surname, self.message,self.created_date)

