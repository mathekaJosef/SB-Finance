from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('print_download/<sale_id>', views.print_download, name='print_download')
]