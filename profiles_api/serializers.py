from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our API  VIew."""
    ## we create a serializer view to accept a name input and then
    # add this to our API view and use it to test post function

    ## it can also validate that the input is correct for the required field
    name = serializers.CharField(max_length=10)
