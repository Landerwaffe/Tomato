from django.conf import settings
from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.register, name="signup"),
    path('login/', views.login, name="login")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)