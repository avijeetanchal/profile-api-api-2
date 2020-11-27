from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


    # """ AS WE HAVE CUSTOMISED THE MODEL WITH EMAIL AND FULL NAME ISTEAD OF EMAIL AND PASS
    # WE HAVE TO MAKE A MANAGER TO INTERACT WITH DJANGO TO TELL HOW TO WORK WITH
    # THE CUSTOM CHANGES MADE."""
class UserProfileManager(BaseUserManager):
    """Manager for USER PROFILES"""

    def create_user(self, email, name, password=None):
        """CREATE A new USER profile"""
        if not email:
            """if email passed is empty string, or null value, the error raise"""
            raise ValueError('user must have an email address')

        #"""second half to be lower case, so standarise it"""
        email = self.normalize_email(email)
        #""" CREATE USER MODEL"""
        user = self.model(email=email, name=name)

        user.set_password(password)
        # """ to keep password encrypted , its converted to hash, and never stored
        # as plain text in a database becoz, the hackers whould able to see
        # hashed passwrod if they retierve your database."""

        user.save(using=self._db)
        #"""SPECIFY THE DATABASE WHICH YOU WANT TO USE"""

        return user


    def create_super_user(self, email, name, password):
        """ create and save a new super user with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True  ## this is INHERITEd by PermissionsMixin
        user.is_staff = True
        user.save(using = self._db)
        return user




# CREATE A NEW CLASS TO INHERIT THE IMPORTED LIB
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    ## for permission system now
    is_active = models.BooleanField(default=True)
    # """User is active or not, default = True"""
    is_staff = models.BooleanField(default=False)
    # staff or not, access to django or not


    # """Model manager for this object, this is becuase to use our custom user model
    # with django CLI so django needs to have to know how to create users, and control users
    # using django CLI tools"""

    objects = UserProfileManager()


    #"""couple of more to our class"""
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name']

    #"""ability to django to retrive fullname of user"""
    def get_full_name(self):
        ### AS WE DEFINE FUNC IN CLASS, WE PUT SELF.
        """rETRIVE full name of user"""
        return self.name

    def get_short_name(self):
        return self.name

    # """ WE NEED TO SPECIFY THE STRING REPRESENTATION OF OUR Model
    # THE ITEM WE WANT TO RETURN WHEN WE CONVERT USER PROFILE OBJECT TO
    # STRING IN PYTHON."""

    def __str__(self):
        """RETURN STRING REPRESNTATION OF OUR USER"""
        return self.email
    # """this is RECOMMENDED FOR ALL DJANGO MODELS BECAUSE OTHERWISE WHEN YOU CONVERT IT TO A
    # STRING, IT WONT NECESSARILY BE A MEANINGFUL OUTPUT SO IN ORDER TO CUSTOMIZE HOW YOU CONVERT
    # THIS TO A STRING YOU WANT TO SPECIFY THIS FUNC AND RETURN THE FIELD THAT
    # YOU WANT TO USE TO IDENTIFY THIS MODEL IF YOU R JUST READING IT IN DJANGO ADMIN OR
    # SOME PYTHON CODE"""


    # """SUPER USER IS ADMIN USER THAT WILL HAVE FULL CONTROL AND ABLE TO ACCESS THE DJANGO ADMIN
    # AND SEE ALL THE MODELS IN THE DATABASE"""
