from imaplib import _Authenticator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .views import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from advert.models import *
from hospital.models import PhoneRepairRequest
from django.db.models import Q

#-------------------------------------------------------------------------------------


def User_Login(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        context = {
        "form":form,
        "error":"Kullanıcı adı veya parola hatalı!",
    }
    if form.is_valid():
        New_User = authenticate(username=username, password=password)
        if New_User is None:
            #messages.info(request,"Kullanıcı adı veya parola hatalı!")
            return render(request,"user/login.html",context)
        else:
            login(request,New_User)
            return redirect("home:index")
    return render(request,"user/login.html")

#-------------------------------------------------------------------------------------


def User_Register(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                context = {
                    "error": "Kullanıcı adı zaten kullanılıyor!",
                    "username": username,
                    "email": email,
                    "firstname": firstname,
                    "lastname": lastname,
                    
                }
                return render(request, "user/register.html",context)
            
            if User.objects.filter(email=email).exists():
                context = {
                    "error": "Mail adresi zaten kullanılıyor!",
                    "username": username,
                    "email": email,
                    "firstname": firstname,
                    "lastname": lastname,
                }
                return render(request, "user/register.html",context)
            else:
                    New_User = User.objects.create_user(
                    username=username, email=email, first_name=firstname, last_name=lastname, password=password)
                    is_active_staf=BusinessStaff.objects.create(author=New_User)

                    New_User.save()
                    
                    is_active_staf.save()
                    login(request, New_User)
                    # messages.success(request,"tenks")
                    return redirect("home:index")
        else:
            return render(request, "user/register.html", {
                "error": "Parolalar eşleşmiyor!",
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname
            })
    return render(request,"user/register.html")


#-------------------------------------------------------------------------------------



@login_required(login_url='user:Login')  # Kullanıcı giriş yapmış mı kontrolü
def User_Profil(request, id):
    if id:
        try:
            user = BusinessStaff.objects.get(author_id=id)
            phone_sales = PhoneSales.objects.filter(author_id=id, is_active=True).order_by('-created_date')
            phone_repairs = MobileRepair.objects.filter(author_id=id,is_active=True).order_by('-created_date')
            phone_parts = PhonePart.objects.filter(author_id=id,is_active=True).order_by('-created_date')
            phone_aksesuars = PhoneAksesuar.objects.filter(author_id=id,is_active=True).order_by('-created_date')
            jobfinish_business_count = PhoneRepairRequest.objects.filter(acceptance=True,sender=id,
            jobfinish=True,
            jobfinish_business=True
            ).count()
            phone_sales_count = phone_sales.count()
            phone_repairs_count = phone_repairs.count()
            phone_parts_count = phone_parts.count()
            phone_aksesuars_count = phone_aksesuars.count()
            all_count = phone_sales_count + phone_repairs_count + phone_parts_count + phone_aksesuars_count
            # Assuming is_staff is a boolean field in the BusinessStaff model
            return render(request, 'user/profil.html', {
                'user': user,
                'jobfinish_business_count':jobfinish_business_count,
                'all_count':all_count,
                'phone_sales': phone_sales,
                'phone_repairs': phone_repairs,
                'phone_parts': phone_parts,
                'phone_aksesuars': phone_aksesuars,
           
            })
        except BusinessStaff.DoesNotExist:
            # Kullanıcı bulunamadı
            return redirect('home:index')
    else:
        if request.user.is_authenticated:
            user = BusinessStaff.objects.get(author=request.user)
            # Diğer işlemler...
            # ...
        else:
            return redirect('home:index')
    
        return render(request, 'user/profil.html', {
            'user': user,
            # Diğer context verileri...
            # ...
        })
#-------------------------------------------------------------------------------------


# @login_required(login_url="user:Login")
# def User_Info_Save(request):
#     if request.method == 'POST':
#         form = BusinessStaffForm(request.POST, request.FILES)
#         if form.is_valid():
#             business_staff = form.save(commit=False)
#             business_staff.author = request.user
#             business_staff.is_staff = False
#             business_staff.save()
#             return redirect('user:Profil')
#     else:
#         form = BusinessStaffForm()
#     return render(request, 'user/profil.html', {'form': form})




#-------------------------------------------------------------------------------------
@login_required(login_url="user:Login")
def User_Info_Update(request, id):
    try:
        user = BusinessStaff.objects.filter(author_id=id).first()

        if user:
            form = BusinessStaffForm(request.POST or None, instance=user, files=request.FILES)

            if form.is_valid():
                update = form.save(commit=False)
                update.author = request.user

                if 'avatar' in request.FILES:
                    update.avatar = request.FILES['avatar']

                if 'biography' in request.POST:
                    update.biography = request.POST['biography']

                if 'address' in request.POST:
                    update.address = request.POST['address'].upper()  # Address'i büyük harflere dönüştürme

                if 'city' in request.POST:
                    update.city = request.POST['city'].upper() 

                if 'district' in request.POST:
                    update.district = request.POST['district'].upper() 

                if 'office_phone' in request.POST:
                    update.office_phone = request.POST['office_phone']

                if 'mobile_phone' in request.POST:
                    update.mobile_phone = request.POST['mobile_phone']

                if 'social_media_facebook' in request.POST:
                    update.social_media_facebook = request.POST['social_media_facebook']

                if 'social_media_twitter' in request.POST:
                    update.social_media_twitter = request.POST['social_media_twitter']

                if 'social_media_instagram' in request.POST:
                    update.social_media_instagram = request.POST['social_media_instagram']

                if 'social_media_tiktok' in request.POST:
                    update.social_media_tiktok = request.POST['social_media_tiktok']

                # Check the value of is_staff field in the form data
                if 'is_staff' in request.POST:
                    is_staff_value = request.POST['is_staff']
                    update.is_staff = (is_staff_value == 'True')

                # Check if is_active field needs to be updated
                if not update.is_active:
                    update.is_active = True

                update.save()

                return redirect('user:Profil', id=id)
            else:
                return render(request, 'user/profil.html', {'user': user, 'form': form})
        else:
            raise Http404

    except Http404:
        return render(request, 'user/profil.html')

#-------------------------------------------------------------------------------------



@login_required(login_url="user:Login")
def Profil_Advert(request):
    # try:
    #     if request.user.is_authenticated:
    #         user_id = request.user.id
    #     user=PhoneSales.objects.filter( author_id=user_id,is_active=True)


    # except Http404:
    #     # Eğer kullanıcı yoksa, aynı sayfayı döndürür
    #     return render(request, 'user/profil.html')
    # user2= User.objects.get(id=user_id)
    # full_name = user2.get_full_name()
    
    # # Kullanıcı varsa, ayrıntıları göstermek için şablonu döndürür
    # return render(request, 'user/profil.html', {'user_id': user,'full_name':full_name})

    try:
        if request.user.is_authenticated:
            user = request.user.id
           
            phone_sales = PhoneSales.objects.filter(author=user, is_active=True)
            return render(request, 'user/profil.html', {'phone_sales': phone_sales})
    except PhoneSales.DoesNotExist:
        return render(request, 'user/profil.html', {'phone_sales': None})







#-------------------------------------------------------------------------------------

def logoutView(request):
    logout (request)
    return redirect("home:index")


#-------------------------------------------------------------------------------------
