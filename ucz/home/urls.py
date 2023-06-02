from django.urls import path
from .import views

app_name="home"
urlpatterns = [
    path('',views.index,name="index"),
    # path('about/',views.about,name="about"),
    # path('contact/',views.contact,name="contact"),
    # path('error/',views.error,name="error"),
    path('search', views.search_view, name='search'),
    path('contactform',views.Contact_Form, name='Contact_Form'),
    path('security',views.Security, name='Security'),
    path('conditions',views.Conditions, name='Conditions')

]
