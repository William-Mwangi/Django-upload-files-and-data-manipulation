"""upload_Files URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from administrator import views
#from .views import MyModelDeleteView, upload, display_data, display_data_with_checkbox, delete_all_objects


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),
    path('uploaded_data/', views.display_data , name="uploaded_data"),
    path('checkbox_uploaded_data/', views.display_data_with_checkbox , name="checkbox_uploaded_data"),
    path('delete_objects/', views.delete_all_objects, name = "delete_all_objects"),
    path('delete_few_objects/', views.delete_selected_objects, name = "delete_selected_objects"),
    path('show_objects/', views.show_objects, name='show_objects'),
    #path('fewer_objects/', views.MyModelDeleteView.as_view(), name = "fewer_objects"),
]
