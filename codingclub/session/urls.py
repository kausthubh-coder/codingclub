
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='sessions'),
    path('/<int:id>', views.sessionpost,name='sessionsbyid'),
    path('/search', views.sessionquery,name='sessionquery'),
]
