from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [

    path('add_toilet/', views.add_toilet, name='add-toilet'),
    path('', views.index, name='index'),
    path('get_toilets/', views.get_toilets, name='get-toilets'),
]