import random
from django.http import Http404
from django.shortcuts import render
from hospital.models import PhoneRepairRequest

from user.models import BusinessStaff
from .models import *
from django.shortcuts import render, get_object_or_404,redirect
from .items import Items
from .forms import PhoneSalesForm, MobileRepairForm,PhonePartForm, PhoneAksesuarForm
# Create your views here.
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

#-------------------------------------------------------------------------------------
@login_required(login_url="user:Login")
def Phone_Sales(request, id):
    items = Items()
    form = PhoneSalesForm(request.POST or None, request.FILES or None)
    user = BusinessStaff.objects.filter(Q(author_id=id) & Q(is_active=True))

    if user:
        if request.method == "POST":
            if form.is_valid():
                phone_sales = form.save(commit=False)
                phone_sales.author = request.user
                phone_sales.city = request.POST.get('city', '').upper()  # City'i büyük harflere dönüştürme
                phone_sales.district = request.POST.get('district', '').upper()

                phone_sales.phone_model = request.POST.get('phone_model', '').upper()  # City'i büyük harflere dönüştürme
                phone_sales.phone_brand = request.POST.get('phone_brand', '').upper()
                phone_sales.save()
                messages.success(request, "İlanınız Alınmıştır, İncelendikten sonra yayına alınacaktır")
                return redirect('advert:Phone_Sales', id=id)
            else:
                messages.error(request, "Lütfen gerekli tüm alanları doldurun.")
        else:
            form = PhoneSalesForm()
    else:
        return redirect('home:index')

    context = {
        'form': form,
        'swap_lists': items.swap,
        'os_lists': items.os,
        'ram_memory_lists': items.ram_memory,
        'memory_lists': items.memory_memory,
        'situation_lists': items.situation,
        'garanti_lists': items.garanti,
    }
    return render(request, "adverts/phone_sale_adverts.html", context)



#-------------------------------------------------------------------------------------
@login_required(login_url="user:Login")
def Phone_Repair(request, id):
    form = MobileRepairForm(request.POST or None, request.FILES or None)
    user = BusinessStaff.objects.filter(Q(author_id=id) & Q(is_active=True))

    if user:
        if request.method == "POST":
            if form.is_valid():
                phone_repair = form.save(commit=False)
                phone_repair.author = request.user
                phone_repair.city = request.POST.get('city', '').upper()  # City'i büyük harflere dönüştürme
                phone_repair.district = request.POST.get('district', '').upper()

                phone_repair.phone_model = request.POST.get('phone_model', '').upper()  # City'i büyük harflere dönüştürme
                phone_repair.phone_brand = request.POST.get('phone_brand', '').upper()

                phone_repair.save()
                messages.success(request, "İlanınız Alınmıştır, İncelendikten sonra yayına alınacaktır")
                return redirect('advert:Phone_Repair', id=id)

            else:
                messages.error(request, "Lütfen gerekli tüm alanları doldurun.")
        else:
            form = MobileRepairForm()
    else:
        return redirect('home:index')

    context = {
        'form': form,
    }
    return render(request, 'adverts/phone_repair_adverts.html', context)

     


#-------------------------------------------------------------------------------------
@login_required(login_url="user:Login")
def Phone_Part(request, id):
    items = Items()
    form = PhonePartForm(request.POST or None, request.FILES or None)
    user = BusinessStaff.objects.filter(Q(author_id=id) & Q(is_active=True))

    if user:
        if request.method == "POST":
            if form.is_valid():
                phone_part = form.save(commit=False)
                phone_part.author = request.user
                phone_part.city = request.POST.get('city', '').upper()  # City'i büyük harflere dönüştürme
                phone_part.district = request.POST.get('district', '').upper()  # District'ü büyük harflere dönüştürme
                phone_part.part_name = request.POST.get('part_name', '').upper() 
                phone_part.save()
                messages.success(request, "İlanınız Alınmıştır, İncelendikten sonra yayına alınacaktır")
                return redirect('advert:Phone_Part', id=id)
            else:
                messages.error(request, "Lütfen gerekli tüm alanları doldurun.")
        else:
            form = PhonePartForm()
    else:
        return redirect('home:index')

    context = {
        'form': form,
        'swap_lists': items.swap,
        'situation_lists': items.situation,
        'garanti_lists': items.garanti,
    }
    return render(request, 'adverts/phone_part_adverts.html', context)


#-------------------------------------------------------------------------------------
@login_required(login_url="user:Login")
def Phone_Aksesuar(request, id):
    items = Items()
    form = PhoneAksesuarForm(request.POST or None, request.FILES or None)
    user = BusinessStaff.objects.filter(Q(author_id=id) & Q(is_active=True))
    
    if user:
        if request.method == "POST":
            if form.is_valid():
                phone_part = form.save(commit=False)
                phone_part.author = request.user
                phone_part.city = request.POST.get('city', '').upper()  # City'i büyük harflere dönüştürme
                phone_part.district = request.POST.get('district', '').upper()  # District'ü büyük harflere dönüştürme
                phone_part.aksesuar_name = request.POST.get('aksesuar_name', '').upper()  # District'ü büyük harflere dönüştürme
                phone_part.save()
                messages.success(request, "İlanınız Alınmıştır, İncelendikten sonra yayına alınacaktır")
                return redirect('advert:Phone_Aksesuar', id=id)
            else:
                messages.error(request, "Lütfen gerekli tüm alanları doldurun.")
        else:
            form = PhoneAksesuarForm()
    else:
        return redirect('home:index')

    context = {
        'form': form,
        'situation_lists': items.situation,
    }
    return render(request, 'adverts/phone_aksesuar_adverts.html', context)




#-------------------------------------------------------------------------------------

#-----------------------------ADVERTS DETAİLS-----------------------------------------

def Phone_Sales_Details(request,id):
    # product = get_object_or_404(PhoneSales, id=id)
    # return render(request, 'adverts/detail.html', {'product': product})
    try:
        total_count_PhoneSales = PhoneSales.objects.filter(is_active=True).count()
        total_count_MobileRepair = MobileRepair.objects.filter(is_active=True).count()
        total_count_PhonePart = PhonePart.objects.filter(is_active=True).count()
        total_count_PhoneAksesuar = PhoneAksesuar.objects.filter(is_active=True).count()

        context = {}  # Boş bir context sözlüğü tanımla

        if total_count_PhoneSales > 0 or total_count_MobileRepair > 0 or total_count_PhonePart > 0 or total_count_PhoneAksesuar > 0:
            # Diğer işlemler
            if total_count_PhoneAksesuar > 0:
                random_index_PhoneAksesuar = random.randint(0, total_count_PhoneAksesuar - 1)
                random_PhoneAksesuar = PhoneAksesuar.objects.all()[random_index_PhoneAksesuar]
                user_PhoneAksesuar = random_PhoneAksesuar.author
                full_name_PhoneAksesuar = user_PhoneAksesuar.get_full_name()
                context['random_PhoneAksesuar'] = random_PhoneAksesuar
                context['full_name_PhoneAksesuar'] = full_name_PhoneAksesuar

            if total_count_PhonePart > 0:
                random_index_PhonePart = random.randint(0, total_count_PhonePart - 1)
                random_PhonePart = PhonePart.objects.all()[random_index_PhonePart]
                user_PhonePart = random_PhonePart.author
                full_name_PhonePart = user_PhonePart.get_full_name()
                context['random_PhonePart'] = random_PhonePart
                context['full_name_PhonePart'] = full_name_PhonePart

            if total_count_MobileRepair > 0:
                random_index_MobileRepair = random.randint(0, total_count_MobileRepair - 1)
                random_MobileRepair = MobileRepair.objects.all()[random_index_MobileRepair]
                user_MobileRepair = random_MobileRepair.author
                full_name_MobileRepair = user_MobileRepair.get_full_name()
                context['random_MobileRepair'] = random_MobileRepair
                context['full_name_MobileRepair'] = full_name_MobileRepair

            if total_count_PhoneSales > 0:
                random_index_PhoneSales = random.randint(0, total_count_PhoneSales - 1)
                random_phonesale = PhoneSales.objects.all()[random_index_PhoneSales]
                user_PhoneSales = random_phonesale.author
                full_name_PhoneSales = user_PhoneSales.get_full_name()
                context['random_phonesale'] = random_phonesale
                context['full_name_PhoneSales'] = full_name_PhoneSales




        product = get_object_or_404(PhoneSales, id=id, is_active=True)
        user = product.author  # Kullanıcıyı al
        full_name = user.get_full_name()  # Tam adı al
        context ['product']=product
        context ['full_name']=full_name
        context ['user']=user
        return render(request, 'adverts_details/phone_sales_details.html', context)
    except:
        # Ürün bulunamazsa index.html sayfasına yönlendirme yap
        return redirect('home:index')

#-------------------------------------------------------------------------------------

def Phone_Repair_Details(request,id):
    try:
        total_count_PhoneSales = PhoneSales.objects.filter(is_active=True).count()
        total_count_MobileRepair = MobileRepair.objects.filter(is_active=True).count()
        total_count_PhonePart = PhonePart.objects.filter(is_active=True).count()
        total_count_PhoneAksesuar = PhoneAksesuar.objects.filter(is_active=True).count()

        context = {}  # Boş bir context sözlüğü tanımla

        if total_count_PhoneSales > 0 or total_count_MobileRepair > 0 or total_count_PhonePart > 0 or total_count_PhoneAksesuar > 0:
            # Diğer işlemler
            if total_count_PhoneAksesuar > 0:
                random_index_PhoneAksesuar = random.randint(0, total_count_PhoneAksesuar - 1)
                random_PhoneAksesuar = PhoneAksesuar.objects.all()[random_index_PhoneAksesuar]
                user_PhoneAksesuar = random_PhoneAksesuar.author
                full_name_PhoneAksesuar = user_PhoneAksesuar.get_full_name()
                context['random_PhoneAksesuar'] = random_PhoneAksesuar
                context['full_name_PhoneAksesuar'] = full_name_PhoneAksesuar

            if total_count_PhonePart > 0:
                random_index_PhonePart = random.randint(0, total_count_PhonePart - 1)
                random_PhonePart = PhonePart.objects.all()[random_index_PhonePart]
                user_PhonePart = random_PhonePart.author
                full_name_PhonePart = user_PhonePart.get_full_name()
                context['random_PhonePart'] = random_PhonePart
                context['full_name_PhonePart'] = full_name_PhonePart

            if total_count_MobileRepair > 0:
                random_index_MobileRepair = random.randint(0, total_count_MobileRepair - 1)
                random_MobileRepair = MobileRepair.objects.all()[random_index_MobileRepair]
                user_MobileRepair = random_MobileRepair.author
                full_name_MobileRepair = user_MobileRepair.get_full_name()
                context['random_MobileRepair'] = random_MobileRepair
                context['full_name_MobileRepair'] = full_name_MobileRepair

            if total_count_PhoneSales > 0:
                random_index_PhoneSales = random.randint(0, total_count_PhoneSales - 1)
                random_phonesale = PhoneSales.objects.all()[random_index_PhoneSales]
                user_PhoneSales = random_phonesale.author
                full_name_PhoneSales = user_PhoneSales.get_full_name()
                context['random_phonesale'] = random_phonesale
                context['full_name_PhoneSales'] = full_name_PhoneSales

        busines_s=BusinessStaff.objects.filter(author_id=request.user.id,is_staff=True)
        waits=PhoneRepairRequest.objects.filter(sender=request.user.id)
        product = get_object_or_404(MobileRepair, id=id,is_active=True)
        user = product.author  # Kullanıcıyı al
        full_name = user.get_full_name()  # Tam adı al

        context['product']= product
        context['full_name']= full_name
        context['user']=user
        context['busines_s']=busines_s
        context['waits']=waits
        return render(request, 'adverts_details/phone_repair_details.html',context)
    except:
        # Ürün bulunamazsa index.html sayfasına yönlendirme yap
        return redirect('home:index')



#-------------------------------------------------------------------------------------



def Phone_Part_Details(request,id):
    try:
        total_count_PhoneSales = PhoneSales.objects.filter(is_active=True).count()
        total_count_MobileRepair = MobileRepair.objects.filter(is_active=True).count()
        total_count_PhonePart = PhonePart.objects.filter(is_active=True).count()
        total_count_PhoneAksesuar = PhoneAksesuar.objects.filter(is_active=True).count()

        context = {}  # Boş bir context sözlüğü tanımla

        if total_count_PhoneSales > 0 or total_count_MobileRepair > 0 or total_count_PhonePart > 0 or total_count_PhoneAksesuar > 0:
            # Diğer işlemler
            if total_count_PhoneAksesuar > 0:
                random_index_PhoneAksesuar = random.randint(0, total_count_PhoneAksesuar - 1)
                random_PhoneAksesuar = PhoneAksesuar.objects.all()[random_index_PhoneAksesuar]
                user_PhoneAksesuar = random_PhoneAksesuar.author
                full_name_PhoneAksesuar = user_PhoneAksesuar.get_full_name()
                context['random_PhoneAksesuar'] = random_PhoneAksesuar
                context['full_name_PhoneAksesuar'] = full_name_PhoneAksesuar

            if total_count_PhonePart > 0:
                random_index_PhonePart = random.randint(0, total_count_PhonePart - 1)
                random_PhonePart = PhonePart.objects.all()[random_index_PhonePart]
                user_PhonePart = random_PhonePart.author
                full_name_PhonePart = user_PhonePart.get_full_name()
                context['random_PhonePart'] = random_PhonePart
                context['full_name_PhonePart'] = full_name_PhonePart

            if total_count_MobileRepair > 0:
                random_index_MobileRepair = random.randint(0, total_count_MobileRepair - 1)
                random_MobileRepair = MobileRepair.objects.all()[random_index_MobileRepair]
                user_MobileRepair = random_MobileRepair.author
                full_name_MobileRepair = user_MobileRepair.get_full_name()
                context['random_MobileRepair'] = random_MobileRepair
                context['full_name_MobileRepair'] = full_name_MobileRepair

            if total_count_PhoneSales > 0:
                random_index_PhoneSales = random.randint(0, total_count_PhoneSales - 1)
                random_phonesale = PhoneSales.objects.all()[random_index_PhoneSales]
                user_PhoneSales = random_phonesale.author
                full_name_PhoneSales = user_PhoneSales.get_full_name()
                context['random_phonesale'] = random_phonesale
                context['full_name_PhoneSales'] = full_name_PhoneSales

        product = get_object_or_404(PhonePart, id=id,is_active=True)
        user = product.author  # Kullanıcıyı al
        full_name = user.get_full_name()  # Tam adı al
        context ['product']=product
        context ['full_name']=full_name
        context ['user']=user
            
        return render(request, 'adverts_details/phone_part_details.html',context)
    except:
        # Ürün bulunamazsa index.html sayfasına yönlendirme yap
        return redirect('home:index')

#-------------------------------------------------------------------------------------



def Phone_Aksesuar_Details(request, id):
    try:
        total_count_PhoneSales = PhoneSales.objects.filter(is_active=True).count()
        total_count_MobileRepair = MobileRepair.objects.filter(is_active=True).count()
        total_count_PhonePart = PhonePart.objects.filter(is_active=True).count()
        total_count_PhoneAksesuar = PhoneAksesuar.objects.filter(is_active=True).count()

        context = {}  # Boş bir context sözlüğü tanımla

        if total_count_PhoneSales > 0 or total_count_MobileRepair > 0 or total_count_PhonePart > 0 or total_count_PhoneAksesuar > 0:
            # Diğer işlemler
            if total_count_PhoneAksesuar > 0:
                random_index_PhoneAksesuar = random.randint(0, total_count_PhoneAksesuar - 1)
                random_PhoneAksesuar = PhoneAksesuar.objects.all()[random_index_PhoneAksesuar]
                user_PhoneAksesuar = random_PhoneAksesuar.author
                full_name_PhoneAksesuar = user_PhoneAksesuar.get_full_name()
                context['random_PhoneAksesuar'] = random_PhoneAksesuar
                context['full_name_PhoneAksesuar'] = full_name_PhoneAksesuar

            if total_count_PhonePart > 0:
                random_index_PhonePart = random.randint(0, total_count_PhonePart - 1)
                random_PhonePart = PhonePart.objects.all()[random_index_PhonePart]
                user_PhonePart = random_PhonePart.author
                full_name_PhonePart = user_PhonePart.get_full_name()
                context['random_PhonePart'] = random_PhonePart
                context['full_name_PhonePart'] = full_name_PhonePart

            if total_count_MobileRepair > 0:
                random_index_MobileRepair = random.randint(0, total_count_MobileRepair - 1)
                random_MobileRepair = MobileRepair.objects.all()[random_index_MobileRepair]
                user_MobileRepair = random_MobileRepair.author
                full_name_MobileRepair = user_MobileRepair.get_full_name()
                context['random_MobileRepair'] = random_MobileRepair
                context['full_name_MobileRepair'] = full_name_MobileRepair

            if total_count_PhoneSales > 0:
                random_index_PhoneSales = random.randint(0, total_count_PhoneSales - 1)
                random_phonesale = PhoneSales.objects.all()[random_index_PhoneSales]
                user_PhoneSales = random_phonesale.author
                full_name_PhoneSales = user_PhoneSales.get_full_name()
                context['random_phonesale'] = random_phonesale
                context['full_name_PhoneSales'] = full_name_PhoneSales

        product = get_object_or_404(PhoneAksesuar, id=id, is_active=True)
        user = product.author  # Kullanıcıyı al
        full_name = user.get_full_name()  # Tam adı al

        context['product'] = product
        context['full_name'] = full_name
        context['user'] = user

        return render(request, 'adverts_details/phone_aksesuar_details.html', context)
    except PhoneAksesuar.DoesNotExist:
        # Ürün bulunamazsa home:index sayfasına yönlendirme yap
        return redirect('home:index')

#-----------------------------ADVERTS DETAİLS-----------------------------------------
