"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls import handler404, handler500
from home.views import handle_not_found
from django.conf import settings #add this
from django.conf.urls.static import static #add this
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('user/', include("user.urls")),
    path('chat/', include("chat.urls")),
    path('advert/', include("advert.urls")),
    path('hospital/', include("hospital.urls")),
    # path('not-found/', handle_not_found, name='handle_not_found'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'home.views.handle_not_found'