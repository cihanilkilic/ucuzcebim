from django import forms
from .models import PhoneSales,MobileRepair, PhonePart,PhoneAksesuar

class PhoneSalesForm(forms.ModelForm):
    class Meta:
        model = PhoneSales
        fields = ('phone_brand', 'phone_model', 'os', 'ram_memory', 'memory_memory', 'situation',
                  'garanti', 'swap', 'city', 'district', 'price', 'comment', 'avatar')

    def clean_phone_brand(self):
        phone_brand = self.cleaned_data.get('phone_brand')
        if not phone_brand:
            raise forms.ValidationError("Telefon Markası boş bırakılamaz.")
        return phone_brand

    def clean_phone_model(self):
        phone_model = self.cleaned_data.get('phone_model')
        if not phone_model:
            raise forms.ValidationError("Telefon Modeli boş bırakılamaz.")
        return phone_model



    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city:
            raise forms.ValidationError("İl boş bırakılamaz.")
        return city

    def clean_district(self):
        district = self.cleaned_data.get('district')
        if not district:
            raise forms.ValidationError("İlçe boş bırakılamaz.")
        return district

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if not price:
            raise forms.ValidationError("Fiyat boş bırakılamaz.")
        return price

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if not comment:
            raise forms.ValidationError("Açıklama boş bırakılamaz.")
        return comment

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if not avatar:
            raise forms.ValidationError("İlan Resmi boş bırakılamaz.")
        return avatar


    # def clean_os(self):
    #     os = self.cleaned_data.get('os')
    #     if not os:
    #         raise forms.ValidationError("Telefon İşletim Sistemi boş bırakılamaz.")
    #     return os

    # def clean_ram_memory(self):
    #     ram_memory = self.cleaned_data.get('ram_memory')
    #     if not ram_memory:
    #         raise forms.ValidationError("Telefon Ram Bellek boş bırakılamaz.")
    #     return ram_memory

    # def clean_memory_memory(self):
    #     memory_memory = self.cleaned_data.get('memory_memory')
    #     if not memory_memory:
    #         raise forms.ValidationError("Telefon Hafıza Bellek boş bırakılamaz.")
    #     return memory_memory

    # def clean_situation(self):
    #     situation = self.cleaned_data.get('situation')
    #     if not situation:
    #         raise forms.ValidationError("Telefon Durumu boş bırakılamaz.")
    #     return situation

    # def clean_garanti(self):
    #     garanti = self.cleaned_data.get('garanti')
    #     if not garanti:
    #         raise forms.ValidationError("Garanti boş bırakılamaz.")
    #     return garanti

    # def clean_swap(self):
    #     swap = self.cleaned_data.get('swap')
    #     if not swap:
    #         raise forms.ValidationError("Takas Durumu boş bırakılamaz.")
    #     return swap

#---------------------------------------------------------------------------------------------

class MobileRepairForm(forms.ModelForm):
    class Meta:
        model = MobileRepair
        fields = [
        'phone_brand','phone_model', 
        'city','district', 
        'avatar','comment']

#---------------------------------------------------------------------------------------------
class PhonePartForm(forms.ModelForm):
    class Meta:
        model = PhonePart
        fields = ['part_name','situation','garanti','swap','city','district','price','comment','avatar'] # Tüm alanları kullanmak isterseniz '__all__' kullanabilirsiniz

#---------------------------------------------------------------------------------------------

class PhoneAksesuarForm(forms.ModelForm):
    class Meta:
         model = PhoneAksesuar
         fields =['aksesuar_name','situation','city','district','price','comment','avatar']
