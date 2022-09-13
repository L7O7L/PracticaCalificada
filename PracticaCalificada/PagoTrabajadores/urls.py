from django.urls import path

from . import views

app_name = 'PagoTrabajadores'

urlpatterns = [

    path('', views.index, name="index"),
    path('calcular_pago', views.calcular_pago, name="calcular_pago"),
    path('resultados', views.resultados, name="resultados"),
    path('login', views.login, name="login"),
    path('calcular', views.calcular, name="calcular"),
    

]