from django.urls import path

from . import views
app_name='bankingapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login.html'),
    path('register/',views.register,name='register.html'),
    path('click_button/',views.click,name='click'),
    path('newuser/',views.newuser,name='registration_form.html'),
    path('message/',views.message,name='message.html'),
]