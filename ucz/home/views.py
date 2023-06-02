from django.contrib import messages
import random

from django.shortcuts import redirect, render
from django.db.models import Q
from advert.models import MobileRepair, PhoneSales, PhonePart, PhoneAksesuar
from django.db.models import Q

from user.models import BusinessStaff
from .forms import *
# Create your views here.
def handle_not_found(request, exception):
    return render(request, 'error_404_/error_404_.html')


def index(request):
    total_count_PhoneSales = PhoneSales.objects.filter(is_active=True).count()
    total_count_MobileRepair = MobileRepair.objects.filter(is_active=True).count()
    total_count_PhonePart = PhonePart.objects.filter(is_active=True).count()
    total_count_PhoneAksesuar = PhoneAksesuar.objects.filter(is_active=True).count()

    context = {}  # Declare an empty context dictionary

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

    return render(request, "home/index.html", context)






def Security(request):

        return render(request,"home/security.html")


def Conditions(request):

    return render(request,"home/conditions.html")


def Contact_Form(request):
    if request.method == 'POST':
        form = ContactModelForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesaj bilgileriniz başarıyla gönderildi. En kısa zamanda dönüş sağlanılacaktır...")
            return redirect('home:Contact_Form')
        else:
            # Invalid form, display error message and pass the form back to the template
            messages.error(request, "Lütfen gerekli tüm alanları doldurun.")
    
    return render(request, "home/contactform.html")

import re

# def normalize_query(query):
#     replacements = {
#         'ı': '[ıI]',
#         'İ': '[iİ]',
#         'ş': '[şŞ]',
#         'Ş': '[şŞ]',
#         'ğ': '[ğĞ]',
#         'Ğ': '[ğĞ]',
#         'ü': '[üÜ]',
#         'Ü': '[üÜ]',
#         'ö': '[öÖ]',
#         'Ö': '[öÖ]',
#         'ç': '[çÇ]',
#         'Ç': '[çÇ]',
#     }

#     for char, replacement in replacements.items():
#         query = re.sub(char, replacement, query)

#     return query

def normalize_query(query):
    replacements = {
        'ı': '[ıI]',
        'İ': '[iİ]',
        'ş': '[şŞ]',
        'Ş': '[şŞ]',
        'ğ': '[ğĞ]',
        'Ğ': '[ğĞ]',
        'ü': '[üÜ]',
        'Ü': '[üÜ]',
        'ö': '[öÖ]',
        'Ö': '[öÖ]',
        'ç': '[çÇ]',
        'Ç': '[çÇ]',
    }

    for char, replacement in replacements.items():
        query = re.sub(char, replacement, query)

    return query

def search_view(request):
    query = request.GET.get('query')
    if query == "":
        return redirect('/')

    query = normalize_query(query)

    mobile_repairs = search_mobile_repair(query)
    phone_sales = search_phone_sales(query)
    phone_parts = search_phone_part(query)
    phone_aksesuars = search_phone_aksesuar(query)
    business_staff = search_business_staff(query)

    return render(request, 'home/search.html', {
        'mobile_repairs': mobile_repairs,
        'phone_sales': phone_sales,
        'phone_parts': phone_parts,
        'phone_aksesuars': phone_aksesuars,
        'business_staff': business_staff,
    })

def search_mobile_repair(query):
    normalized_query = normalize_query(query)
    results = MobileRepair.objects.filter(
        Q(phone_brand__iregex=normalized_query) |
        Q(phone_model__iregex=normalized_query) |
        Q(city__iregex=normalized_query) |
        Q(label__iregex=normalized_query) |
        Q(district__iregex=normalized_query) |
        Q(author__first_name__iregex=normalized_query) |
        Q(author__last_name__iregex=normalized_query) |
        Q(comment__iregex=normalized_query)
    ).filter(is_active=True)

    # Add author's full name to the results
    for repair in results:
        repair.author_full_name = f"{repair.author.first_name} {repair.author.last_name}"

    return results

def search_phone_sales(query):
    normalized_query = normalize_query(query)
    results = PhoneSales.objects.filter(
        Q(phone_brand__iregex=normalized_query) |
        Q(phone_model__iregex=normalized_query) |
        Q(city__iregex=normalized_query) |
        Q(label__iregex=normalized_query) |
        Q(district__iregex=normalized_query) |
        Q(author__first_name__iregex=normalized_query) |
        Q(author__last_name__iregex=normalized_query) |
        Q(comment__iregex=normalized_query)
    ).filter(is_active=True)

    # Add author's full name to the results
    for sale in results:
        sale.author_full_name = f"{sale.author.first_name} {sale.author.last_name}"

    return results

def search_phone_part(query):
    normalized_query = normalize_query(query)
    results = PhonePart.objects.filter(
        Q(part_name__iregex=normalized_query) |
        Q(city__iregex=normalized_query) |
        Q(label__iregex=normalized_query) |
        Q(author__first_name__iregex=normalized_query) |
        Q(author__last_name__iregex=normalized_query) |
        Q(district__iregex=normalized_query)
    ).filter(is_active=True)

    # Add author's full name to the results
    for part in results:
        part.author_full_name = f"{part.author.first_name} {part.author.last_name}"

    return results

def search_phone_aksesuar(query):
    normalized_query = normalize_query(query)
    results = PhoneAksesuar.objects.filter(
        Q(aksesuar_name__iregex=normalized_query) |
        Q(city__iregex=normalized_query) |
        Q(district__iregex=normalized_query) |
        Q(label__iregex=normalized_query) |
        Q(comment__iregex=normalized_query) |
        Q(author__first_name__iregex=normalized_query) |
        Q(author__last_name__iregex=normalized_query)
    ).filter(is_active=True)

    # Add author's full name to the results
    for aksesuar in results:
        aksesuar.author_full_name = f"{aksesuar.author.first_name} {aksesuar.author.last_name}"

    return results

def search_business_staff(query):
    normalized_query = normalize_query(query)
    results = BusinessStaff.objects.filter(
        Q(author__username__iregex=normalized_query) |
        Q(author__first_name__iregex=normalized_query) |
        Q(author__last_name__iregex=normalized_query) |
        Q(address__iregex=normalized_query)
    ).filter(is_active=True)

    # Add full name and avatar to the results
    for staff_member in results:
        staff_member.author_name = f"{staff_member.author.first_name} {staff_member.author.last_name}"
        staff_member.avatar_url = staff_member.author.avatar.url if hasattr(staff_member.author, 'avatar') else None

    return results


