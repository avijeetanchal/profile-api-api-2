from rest_framework import serializers

from profiles_api import models ## this will allow us to access our user profile
## model that we created

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our API  VIew."""
    ## we create a serializer view to accept a name input and then
    # add this to our API view and use it to test post function

    ## it can also validate that the input is correct for the required field
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes the USer profiles object"""

    class Meta:
        model = models.UserProfile ## this sets our serializer up to point
        ## to our UserProfile model...
        fields = ('id','email','name','password')
        # this is name of fileds which we want to work with
        # but we dont want any user to retrieve password, only while creating
        extra_kwargs ={
            'password':{
                'write_only':True, # so when we do get we wont get passwrd field
                'style':{'input_type':'password'}
            }
        }

        ## now we over write the create method provided by django to hash the password
        ## becuase we are dealing with USER PROFILES API... need security
    def create(self, validated_data):
        """Create and return a new USER"""
        ## make sure its ourside meta class
        user = models.UserProfile.objects.create_user( ## create_user is define in models.py
            email=validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Srializes Profile FEED ITEMS"""
    ## set our profile feed item to our profile feed item class
    class Meta:
        model = models.ProfileFeedItem
        # set to our profile feed item modle that we created in models.py
        # which has 3 fields : user_profile, status_text and created_on

        fields = ('id','user_profile','status_text','created_on')
        # id is created by django automatically as READ ONLY
        # created_on is also READ ONLY, rest two are wrtiable
        # we create user profile based on the authenticated user who has logged in
        extra_kwargs = {'user_profile':{'read_only':True}}

        #### END of serializer for a new model
        
