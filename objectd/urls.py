from django.urls import include, path
from . import views

app_name='objectd'

urlpatterns = [
    path('', views.index, name="index"),
    # path('Charge', views.chargement, name="chargment"),
    path("<int:id>", views.show, name="show"), # Passage du parametre id qui est

]
