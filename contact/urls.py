from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index')    # importa a view Index de views e dá um nome para ela 
]