from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import *
from user.models import BusinessStaff
from .views import *
from advert .models import MobileRepair
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import re
@login_required(login_url="user:Login")
def MobileRepair_Request(request):
    user = BusinessStaff.objects.filter(author_id=request.user.id, is_staff=True).first()
    if user:
        waits = PhoneRepairRequest.objects.filter(Q(acceptance=False, sender=request.user) | Q(acceptance=True, sender=request.user)).order_by('-created_date')
        if user.address:
            user_city = user.city

            # Türkçe karakterlere duyarlı olmayan düzenli ifade oluşturma fonksiyonu
            def create_regex_pattern(text):
                pattern = ''
                for char in text:
                    pattern += '[' + char.lower() + char.upper() + ']'
                return pattern

            # Kullanıcının şehir adındaki Türkçe karakterleri düzenli ifadelerle değiştirme
            user_city_pattern = create_regex_pattern(user_city)

            phone_repairs = MobileRepair.objects.filter(
                Q(is_active=True) & Q(jobfinish=False) & Q(acceptance=False) & 
                (Q(city__iregex=r'^{0}$'.format(user_city_pattern)) | Q(city__icontains=user.district))
            ).order_by('-created_date')
            
        else:
            phone_repairs = MobileRepair.objects.none()  # Empty queryset when address is not available
        jobfinish_ = PhoneRepairRequest.objects.filter(Q(sender=request.user) & Q(acceptance=True) & (Q(jobfinish=False) | Q(jobfinish=True))).order_by('-created_date')
        return render(request, 'hospital/hospital.html', {
            'user': user,
            'phone_repairs': phone_repairs,
            'waits': waits,
            'jobfinish_': jobfinish_
        })
    else:
        return redirect('home:index')


@login_required(login_url="user:Login")
def MobileRepair_Request_ID(request, id):

        
 
    try:
        phone_repair = get_object_or_404(MobileRepair, id=id)
        
        # Check if a PhoneRepairRequest with the same product already exists
        existing_request = PhoneRepairRequest.objects.filter(product=id).exists()
        if existing_request:
            # Handle the case when a PhoneRepairRequest with the same product already exists
            return redirect("hospital:MobileRepair_Request")
        
        kaydet = PhoneRepairRequest.objects.create(
            sender=request.user, 
            product=id, 
            receiver=phone_repair.author,
            phone_model=phone_repair.phone_model,
            phone_brand=phone_repair.phone_brand,
            city=phone_repair.city,
            district=phone_repair.district,
        )
        kaydet.save()
        return redirect('hospital:MobileRepair_Request')

    except:
        return render(request, "hospital/hospital.html")



@login_required(login_url="user:Login")
def Garage (request):
    user=BusinessStaff.objects.filter(author_id=request.user.id,is_staff=False)
    if user:
        waits=PhoneRepairRequest.objects.filter(Q(acceptance=False) & Q(receiver=request.user.id) | Q(acceptance=True)& Q(receiver=request.user.id))
        waits_with_sender_full_name = []
        for wait in waits:
            sender_full_name = wait.sender.get_full_name()  # Sender'ın full_name alanını al
            waits_with_sender_full_name.append({'request': wait, 'sender_full_name': sender_full_name})

        return render(request, 'hospital/garage.html', {
        'user_id': user,
        'waits':waits_with_sender_full_name

        })
   
    else:    # Eğer kullanıcı yoksa, aynı sayfayı döndürür
        if user:
        
            return redirect('user:Profil')
        else:
            return redirect('user:Profil')
    # return render(request,'hospital/garage.html')

@login_required(login_url="user:Login")
def Garage_Acceptance_Yes(request, id):
    repair_request = get_object_or_404(PhoneRepairRequest, product=id)
    repair_request.acceptance = True
    print(id,"Onayla")
    repair_request_2 = get_object_or_404(MobileRepair, id=id)
    repair_request_2.acceptance = True
    repair_request_2.save()
    
    repair_request.save()
    return redirect('hospital:Garage')

@login_required(login_url="user:Login")
def Garage_Acceptance_No(request,product,sender):
    # print(product,"Reddet",sender)
    repair_request = get_object_or_404(PhoneRepairRequest, product=product, sender=sender)
    repair_request.delete()
    return redirect('hospital:Garage')

@login_required(login_url="user:Login")
def Jobfinish_Business (request,product,receiver):
    jobfinish_business_ = get_object_or_404(PhoneRepairRequest, product=product,sender=request.user.id,receiver=receiver)
    jobfinish_business_.jobfinish_business = True
    jobfinish_business_.save()
    
    return redirect('hospital:MobileRepair_Request')

@login_required(login_url="user:Login")
def Jobfinish_Personel(request,product,id):
    jobfinish_personel_ = get_object_or_404(PhoneRepairRequest, product=product,receiver=request.user.id,sender=id)
    jobfinish_personel_.jobfinish = True
    jobfinish_personel_.save()
    return redirect('hospital:Garage')
