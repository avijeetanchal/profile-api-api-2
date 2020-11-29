from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
## next to route specific viewsets with our router we do next code
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset') ## name of our URL for viewsets
## this router will create all of the 4 URLs for us we dont specify a / here
## second argument the viewset we want to registwer,with this URL
## base name --- this is used to retrieve our router if we ever need to do that using URL retrieveing
# function provided by django.
router.register('profile',views.UserProfileViewSet)
## unlike the prvious route ,, we dont need to specify a base_name bcoz we have
# in our vviewset a queryset object , the DRF confires the name provided to
# the modol in the queryset



## url to map different views in our app.
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls))  ## blank -- to include all of the URLs in base URl.

]
# """ the url is mathced and then HelloApiView is sent as view
# in which it will give a get response if get request has been made"""
