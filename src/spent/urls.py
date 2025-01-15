from django.urls import path
from . import views
app_name = 'spent'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/spents', views.spents_by_month, name='spents_by_month'),
]
