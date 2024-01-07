"""Tomato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from .pages import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),  
    path('listings/', views.listings),
    path('contact/', views.contact),
    path('about/', views.about),
    path('listing/<slug:slug>/<int:id>' , views.listing_detail),
    path('', include('accounts.urls')),
    path('profile/', views.profile),
    path('edit/firstname', views.editfirstname),
    path('edit/lastname', views.editlastname),
    path('edit/email', views.editemail),
    path('edit/gender', views.editgender),
    path('edit/password', views.editpassword),
    path('edit/picture', views.editpicture),
    path('query/', views.query),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

