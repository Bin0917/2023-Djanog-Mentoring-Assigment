from django.urls import path
from . import views as views


urlpatterns = [
    path('login/', views.login_view ,name='login_view'),
    path('signup/', views.signup, name='signup_view'),
]
