from django.urls import path
from .import views


app_name="advert"

urlpatterns = [


    path('phonesaless/<int:id>/',views.Phone_Sales, name='Phone_Sales'),
    path('phonerepairr/<int:id>/',views.Phone_Repair, name='Phone_Repair'),
    path('phonepartt/<int:id>/', views.Phone_Part, name='Phone_Part'),
    path('phoneaksesuarr/<int:id>/', views.Phone_Aksesuar, name='Phone_Aksesuar'),
    #---------------------DETAILS----------------------------------
    path('phonesales/<int:id>/', views.Phone_Sales_Details, name='Phone_Sales_Details'),
    path('phonerepair/<int:id>/', views.Phone_Repair_Details, name='Phone_Repair_Details'),
    path('phonepart/<int:id>/', views.Phone_Part_Details, name='Phone_Part_Details'),
    path('phoneaksesuar/<int:id>/',views.Phone_Aksesuar_Details, name='Phone_Aksesuar_Details'),


    
]