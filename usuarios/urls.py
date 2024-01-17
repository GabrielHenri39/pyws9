from django.urls import path
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"), # type: ignore
    path('login/', views.login, name="login"), # type: ignore
    path('logout/', views.logout, name='logout'),

    
]
