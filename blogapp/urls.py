from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('profile',views.profile,name='profile'),
    path('add',views.add,name='add'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('update-bio/', views.update_bio, name='update_bio'),
]