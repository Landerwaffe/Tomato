from django.conf import settings
from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.register, name="signup"),
    path('login/', views.signin, name="login"),
    path('logout/', views.signout, name="logout")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)