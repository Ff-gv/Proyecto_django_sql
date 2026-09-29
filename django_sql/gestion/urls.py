from django.urls import path
from .views import ClienteListView,ClienteCreateView,ClienteDeleteView,ClienteUpdateView
urlpatterns = [
    path('',ClienteListView.as_view(),name='cliente_list'),
    path("cliente/create/",ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update/',ClienteUpdateView.as_view(),name='cliente_update'),
    path('cliente/<int:pk>/delete/',ClienteDeleteView.as_view(),name='cliente_delete'),
]
