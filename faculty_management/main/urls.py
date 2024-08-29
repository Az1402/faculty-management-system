from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_message/', views.send_message, name='send_message'),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('login/', views.login, name='login'),  # Ensure this line is correct
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
