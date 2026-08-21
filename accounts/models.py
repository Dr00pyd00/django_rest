
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    """ 
    Used for create user with EMAIL as login cred 
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email Required!')
        # capitalize and clean email input:
        email = self.normalize_email(email)
        # self.model go take the model attribute of the custom user 
        # model auquel ce manager est rattacher avec :     objects = CustomUserManager()
        user = self.model(email=email, **extra_fields)
        # set the pw
        user.set_password(password)
        # adaptative db 
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # add to extra_fields superuser attributes
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    """ User with EMAIL as principal credential """
    # on retire le username
    username = None
    # force email a etre unique 
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email' # username est par defaut le field auth, la on le remplace
    REQUIRED_FIELDS = []    # pour le CLI create_superuser seulement, ici on laisse simple

    objects = CustomUserManager() # on branche le manager personnaliser ici, il cherhcera le model ici

    def __str__(self):
        return self.email















