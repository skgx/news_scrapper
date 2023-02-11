#first file to get loaded
from django.contrib import admin
from django.urls import include, path
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls'))
]

