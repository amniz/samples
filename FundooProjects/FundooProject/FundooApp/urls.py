from django.urls import path,include
from . import views
from django.urls import re_path
urlpatterns=[
    path('',views.login, name='login'),
    path('home',views.home),
    path('forgot',views.forgot_password,name='forgot'),
    path('activate/<token>/',views.activate, name='activate'),
    path('reset/<token>/',views.reset, name='reset'),
    path('register',views.register,name='register'),
    path('logout',views.logout),
    path('upload',views.upload),
    path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('loginsocial',views.loginsocial),
    path('success',views.success)
    # path('activate/',views.activate,name='activate')
    # path('activate/(?P<token>[0-9A-Za-z]{1,1000}.[0-9A-Za-z]{1,1000}.[0-9A-Za-z]{1,1000})/$',views.activate,name='activate')
]