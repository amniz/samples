from django.urls import path,include
from . import views
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view


# schema_view = get_swagger_view(title='Pastebin API')
urlpatterns=[
    path('',views.login, name='login'),
    path('home',views.home),
    # path('apidoc',schema_view),
    path('forgot',views.forgot_password,name='forgot'),
    path('activate/<token>/',views.activate, name='activate'),
    path('reset/<token>/',views.reset, name='reset'),
    path('register',views.register,name='register'),
    path('logout',views.logout),
    path('upload',views.upload),
    path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('loginsocial',views.loginsocial,name='loginsocial'),
    path('success',views.success),
    path('Note',views.Note.as_view()),
    path('Note/<int:pk>',views.Note.as_view()),
    path('demo',views.demo,name='demo'),
    path('add', views.add, name='add'),
    path('reminder',views.reminder,name='reminder')

    # path('activate/',views.activate,name='activate')
    # path('activate/(?P<token>[0-9A-Za-z]{1,1000}.[0-9A-Za-z]{1,1000}.[0-9A-Za-z]{1,1000})/$',views.activate,name='activate')
]
