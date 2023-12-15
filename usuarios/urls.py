from django.urls import path
from . import views
from django.contrib.auth import views as Authviews

urlpatterns = [
    path('login/', Authviews.LoginView.as_view(template_name='form_auth.html'), name="login"),
    path('singup/', views.signup, name="singup"),
    path('logout/', Authviews.LogoutView.as_view(template_name='form_auth.html'), name="logout"),
    path('meus-anuncios/', views.meus_favoritos, name='meus-livros-favoritos'),
    path('favoritar-livro/<int:livro_id>/',
         views.favoritar_livro, name='favoritar-livro'),
]
