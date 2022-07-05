from django.urls import path
from .import views
urlpatterns = [
   path("newuser",views.add,name='newuser'),
   path("welcome",views.wel,name='welcome page'),
   path("home",views.home,name='home_page')
]