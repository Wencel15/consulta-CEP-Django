from django.urls import path
from .views import consulta_cep


# urlpatterns define os padroes de url
urlpatterns = [
    path('', consulta_cep, name='consulta_cep'),
]

# consulta_cep é a função de view que será chamada para lidar com a requisição HTTP
# name='consulta_cep' nome opcional dado à URL