from django.conf import settings
from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.register, name="signup"),
    path('login/', views.signin, name="login"),
    path('logout/', views.signout, name="logout"),
    path('booking/<slug:slug>/<int:id>', views.booking, name="booking"),
    path('history/', views.history, name="history")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)