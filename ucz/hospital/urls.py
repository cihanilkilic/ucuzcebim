from django.urls import path
from .import views

app_name="hospital"
urlpatterns = [
    path('reapair',views.MobileRepair_Request,name="MobileRepair_Request"),
    path('reapairid/<int:id>',views.MobileRepair_Request_ID,name="MobileRepair_Request_ID"),
    path('garage/',views.Garage,name="Garage"),
    path('garageacceptancey /<int:id>',views.Garage_Acceptance_Yes,name="Garage_Acceptance_Yes"),
    path('garageacceptancen/<int:product>/<int:sender>/', views.Garage_Acceptance_No, name="Garage_Acceptance_No"),
    path('jobfinish/<int:product>/<int:receiver>/', views.Jobfinish_Business, name="Jobfinish_Business"),
    #--------------------------------
    path('jobfinishp/<int:product>/<int:id>/', views.Jobfinish_Personel, name="Jobfinish_Personel"),

   
]
