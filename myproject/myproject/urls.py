from django.contrib import admin
from django.urls import path
from myproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.aurea_view, name='home'),  # URL padrão
    path('aurea/', views.aurea_view, name='aurea'),
]
