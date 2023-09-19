from django.urls import path,include
from .views import *
urlpatterns = [
    path('',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('profile/<int:pk>/',ProfileView.as_view(),name='profile'),
    path('users/<int:pk>/',UserView.as_view(),name='userview'),
    

]
