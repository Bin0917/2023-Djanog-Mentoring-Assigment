from django.urls import path
from . import views as views


urlpatterns = [
    path('writePost/', views.writePost ,name='writePost'),
    # path('signup/', views.signup, name='signup_view'),
    path('showPostList/',views.showPostList, name='showPostList')
]
