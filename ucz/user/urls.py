from django.urls import path
from .import views

app_name="user"
urlpatterns = [
    path('login/',views.User_Login,name="Login"),
    path('register/',views.User_Register,name="Register"),
    path('profil/<int:id>/',views.User_Profil,name="Profil"),
    # path('User_Info_Save/',views.User_Info_Save,name="User_Info_Save"),
    path('User_Info_Update/<int:id>/',views.User_Info_Update,name="User_Info_Update"),


    path('logout/',views.logoutView,name="Logout"),

]
