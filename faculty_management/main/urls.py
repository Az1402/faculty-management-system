from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_message/', views.send_message, name='send_message'),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('login/', views.login_view, name='login'),  # Updated to match the view name
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
