from chat import views
from django.urls import path

urlpatterns=[
    path('',views.login),
    path('register',views.register),
    path('forgotpassword',views.forgot_password),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('reset/<uidb64>/<token>/',views.reset,name='reset'),
    # path('forgot/', views.forgot, name='forgot')
]