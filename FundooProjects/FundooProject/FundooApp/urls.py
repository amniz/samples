from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.login),
    path('forgot',views.forgot_password,name='forgot'),
    path('activate/<token>/',views.activate, name='activate'),
    path('reset/<token>/',views.reset, name='reset'),
    path('register',views.register,name='register'),
    # path('activate/',views.activate,name='activate')
    # path('activate/(?P<token>[0-9A-Za-z]{1,1000}.[0-9A-Za-z]{1,1000}.[0-9A-Za-z]{1,1000})/$',views.activate,name='activate')
]