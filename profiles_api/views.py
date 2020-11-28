from rest_framework.views import APIView, Response
## APIVIEW  ===
## Response === used to responses from the api view


class HelloApiView(APIView):
    """TEST API VIEW"""
    ## allow us to define endpoint logic in this class
    ## you assignan URL and then you assign the URL to this VIEW class AND
    ## DJANGO handles it by calling appropiate func in the view for HHTTP reuqest
    ## APIView is broken up by expect a func for diff HTTP request
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
