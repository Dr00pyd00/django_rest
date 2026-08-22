

# Tuto django / apirest

Pour nvim il faut un file **`pyrightconfig.json`** a la racince du projet pour gerer les erreurs django:
```bash 
{
  "venvPath": ".",
  "venv": ".venv",
  "pythonVersion": "3.14",
  "typeCheckingMode": "basic",
  "reportMissingImports": "warning",
  "reportMissingModuleSource": "none",
  "reportAttributeAccessIssue": "none",
  "reportCallIssue": "none",
  "reportOptionalMemberAccess": "none"
}
```

## Setup le projet:

> creer dossier projet + venv 

1] Installer django et django rest frta;ework ( extention pour les api ) : 
```bash 
pip install django djangorestframework
pip freeze > requirements.txt
```

2] Creer le projet django:
```bash 
django-admin startproject config . 
```
- `config` : nom que je donne a la struct de base 
- `.` : dans le dossier courant

3] Creer une app a ajouter au projet:
```bash 
python3 manage.py startapp library
```

4] Brancher l'app au projet:   
Dans `config/settings.py`:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'library.apps.LibraryConfig',
]
```


## User PRO 

**AVANT LA PREMIERE MIGRATION**

Creation d'un User utilisable en pro !     
1] Creer une app special:
```bash 
python3 manage.py startapp accounts 
```
2] Dans `settings`:   
- brancher l'app via INSTALLED_APPS dans settings.
- ajouter ligne pour detecter le user custom a la place du user par defaut.
```python
# souvent a cote de installed_apps
AUTH_USER_MODEL = 'accounts.CustomUser'
```

3] Creer un Custom user ( + flexible ) et un Manager qui va avec:
```python 
# dans accounts/models.py

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
```


### Migrations 

```bash
python manage.py makemigrations
python manage.py migrate
```

- `makemigrations` : regarde tes modèles actuels (`Author`, `Book`, `CustomUser`...) et **génère les fichiers de migration** correspondants (des fichiers Python dans `library/migrations/` et `accounts/migrations/`) — équivalent de `alembic revision --autogenerate`. Ça ne touche **pas** encore la base de données, ça écrit juste le plan.
- `migrate` : **applique** ces fichiers de migration à la base de données réelle — crée/modifie effectivement les tables. Équivalent de `alembic upgrade head`.



## Serializers 

Sert a passer des objets python en dict  et inversement, pour ensuite les passer en json par exemple.       
```python 
# creer dans l'app : library/serialisers.py 

from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
   class Meta:
        model = Author
        fields = ['id', 'name', 'birth']

class BookSerializer(serializers.ModelSerializer):

    # si jamais on veut que le champ author ai le dict complet et pas que le id:
    # ajouter:
    # author = AuthorSerializer()
    # pas forcement besoin car on a acces a la data si besoin par un autre moyen

    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'year']
```
S'en servir:
```python 
ser = AuthorSerializer(author_object) 
ser.data  # donnees pretes a etre utiliser pour creer un objet plyus tard : dict python

# va return un objet python:
ser2 = BookSerializer(data=author_dict) # preciser 'data=' ABSOLUMENT
ser2.is_valid() # check si les data sont bonnes 
ser2.validated_data # voir les data
ser2.save()
```












