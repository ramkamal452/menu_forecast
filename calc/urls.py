from django.urls import path
from . import views
urlpatterns =[
    path("",views.home,name="home"),  #home is function name
    path("food",views.food,name="food")
]
