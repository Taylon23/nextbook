from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
     path('agendar-livro/<int:livro_id>/', views.agendar_livro, name='agendar_livro'),
]