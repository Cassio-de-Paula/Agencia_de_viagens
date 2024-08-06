from django.urls import path
from app.views.passageiro_views import *
from app.views.voos_views import *
from app.views.home import *

urlpatterns = [
    path('', home, name='home'),
    path('api/list_passageiros/', list_passageiros, name='list_passageiros'),
    path('api/list_voos/', list_voos, name='list_voos'),
    path('api/create_passageiro/', create_passageiro, name='create_passageiro'),
    path('api/create_voo/', create_voo, name='create_voo'),
    path('api/update_passageiro/<int:id>/', update_passageiro, name='update_passageiro'),
    path('api/update_voo/<int:id>/', update_voo, name='update_voo'),
    path('api/delete_passageiro/<int:id>/', delete_passageiro, name='delete_passageiro'),
    path('api/delete_voo/<int:id>/', delete_voo, name='delete_voo'),

    path('api/history_voos/<int:id>/', get_voos_passageiro, name='history_voos'),
    path('api/tripulation/<int:id>/', get_passageiros_voo, name='tripulacao'),

    path('api/add_passageiro_voo/<int:id>/', add_passageiro, name='add_passageiro'),
    path('api/delete_tripulante/<int:passageiro_id>/<int:voo_id>', delete_tripulante, name='delete_tripulante')
]