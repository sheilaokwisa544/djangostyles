# configurations for the url part...second step after pasting the url
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Triggerapp.urls')),
]
