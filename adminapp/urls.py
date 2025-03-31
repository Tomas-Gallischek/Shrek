from django.urls import path
from . import views


urlpatterns = [
    path('', views.adminpage, name='adminpage'),
    path('aktualni_den.html', views.aktualizovat_den),
    path('statistiky_avataru', views.statistiky)
]
