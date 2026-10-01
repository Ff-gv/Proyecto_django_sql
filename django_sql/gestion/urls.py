from django.urls import path
from .views import (ClienteListView,ClienteCreateView,ClienteDeleteView
                    ,ClienteUpdateView,CuentaCreateView,CuentaDeleteView,
                    CuentaListView,CuentaUpdateView,TransaccionCreateView,
                    TransaccionDeleteView,TransaccionListView,TransaccionUpdateView)
urlpatterns = [
    path('',ClienteListView.as_view(),name='cliente_list'),
    path("cliente/create/",ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update/',ClienteUpdateView.as_view(),name='cliente_update'),
    path('cliente/<int:pk>/delete/',ClienteDeleteView.as_view(),name='cliente_delete'),
    path('cuenta/',CuentaListView.as_view(),name='cuenta_list'),
    path('cuenta/create/',CuentaCreateView.as_view(),name='cuenta_create'),
    path('cuenta/<int:pk>/update/',CuentaUpdateView.as_view(),name='cuenta_update'),
    path('cuenta/<int:pk>/delete/',CuentaDeleteView.as_view(),name='cuenta_delete'),
    path('transaccion/',TransaccionListView.as_view(),name='transaccion_list'),
    path('transaccion/create/',TransaccionCreateView.as_view(),name='transaccion_create'),
    path('transaccion/<int:pk>/update/',TransaccionUpdateView.as_view(),name='transaccion_update'),
    path('transaccion/<int:pk>/delete/',TransaccionDeleteView.as_view(),name='transaccion_delete'),      
]
