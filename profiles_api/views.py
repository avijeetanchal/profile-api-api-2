from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
## status is list of handy HTTP status codes
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
# this will be used to authenticate users ,, works by generating random tokens,
# when user loggs in on every request we add this token along
from rest_framework import filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework .permissions import IsAuthenticatedOrReadOnly  ## for feed update 

from profiles_api import serializers
## serializers is used to tell API view what data to expect when make a
# post put patch request
from profiles_api import models

from profiles_api import permissions ## to authenticate we made our logic



## APIVIEW  ===
## Response === used to responses from the api view


class HelloApiView(APIView):
    """TEST API VIEW"""
    ## allow us to define endpoint logic in this class
    ## you assignan URL and then you assign the URL to this VIEW class AND
    ## DJANGO handles it by calling appropiate func in the view for HHTTP reuqest
    ## APIView is broken up by expect a func for diff HTTP request
    serializer_class = serializers.HelloSerializer



    def get(self, request, format=None):
        """Returns a list of APIView features"""
        ## when we run get on the url it call the get function
        ## request object -- passed by django rest frameowrk
        ## contains details of the rest being made to the API
        ## format is json or xml or others
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete).',
        'is similary to traditonal django view',
        'gives you the most control of your API logic',
        'Is mapped manually to URLs',
        ]
        ## can be anything you want to return in your APIVIEW
        ## every http function must return a response.
        ## it is expected by django rest frameowrk

        ## RESPONSE CAN BE DICT OR A LIST
        return Response({'message':'Hello!',
        'an_apiview': an_apiview}) ## response is thus converted to json, so list of dict.

    def post(self,request):
        """ create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        # part of request object that has data for post, put patch

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # to fetch the name field defined in our serializer
            # like this we can get any filed we define in the serializer
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                ) # give dic of error based on validation

    def put(self, request, pk=None):
        """Handle updating Object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle patiral update of Object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pf=None):
        """Handle deleting of Object"""
        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet): # base viewset class that django providwe
    """TEst API viewSets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a Hello message"""
        a_viewset = [
        "USes action such as ('list','create','retrieve','update','partial_update')",
        'automatically maps to URLs using Routers',
        'Provides more functionality with less code'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk =None):
        """Handle updating an OBJECT"""
        return Response({'method':'PUT'})

    def partial_update(self, request, pk=None):
        """ handle uadting partial part"""
        return response({'method':'PATCH'})

    def destroy(self,request,pk=None):
        """ handle deleting an OBJECT"""
        return Response({'method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating Profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    ## DRF knows the standard func you want to perform on a model view set
    ## create and list funcs  , and CRUD also
    authentication_classes = (TokenAuthentication,) #make it tuple
    permission_classes = (permissions.UpdateOwnProfile,) ## variable name is cause errors
    ## if wronf variable name assign to permission_classes

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)



class UserLoginApiView(ObtainAuthToken):
    """ HANDLE creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    ##  it adds renderer classes to our obtain auth token view
    ## which will enable in django admin, the rest of the view sets
    ## we enables ObtainAuthToken by api_settings


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, updating and delete profile feed items"""
    # we gonna use token authentication to authenticate reuqests to out end point
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    # this sets the cerializers class on our view sets

    # we gonna apply query set managed by our view sets
    queryset =  models.ProfileFeedItem.objects.all()

    permission_classes = (
        permissions.UpdateOwnStatus, # this wont allow user to update others status
        IsAuthenticatedOrReadOnly # this permission from DRF
    )

    # manually set a field to read only we do this below
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        ## the perform_create func is handy from django that allows you to
        # override the behvaour for creating objects through a Model view set
        ### THIS IS CALLED EVERY POST REQUEST TO OUR VIEW SET
        serializer.save(user_profile=self.request.user)
        ##
