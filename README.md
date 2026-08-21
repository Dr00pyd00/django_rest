

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






