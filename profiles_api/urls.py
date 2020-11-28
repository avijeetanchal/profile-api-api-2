from django.urls import path
from profiles_api import views

## url to map different views in our app.
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
# """ the url is mathced and then HelloApiView is sent as view
# in which it will give a get response if get request has been made"""
