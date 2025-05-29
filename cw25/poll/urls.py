from django.urls import path, include
from poll import views

app_name = 'poll'

urlpatterns = [
    path('', views.show_question, name='show_question')
]