


# A la sortie de la DB c'est un objet python qui sort 
# Mais HTTP et tout dois gerer du texte 
# avec ModelSerializer : calque les champs du models pour en faire le Serializer
# On precise le model donc l'objet et les fields:
# fields = [...] : liste explicite des champs exposés en JSON — toujours explicite, jamais '__all__', 
# pour ne jamais exposer un champ sensible ajouté plus tard par erreur

# attention dans le shell si on fait l'inverse  ser -> book 
# bb = BookSerializer(data=s.data)   # bb : objet BookSerializer, données pas encore validées
# bb.is_valid()                       # déclenche la validation, bb reste un BookSerializer
# bb.validated_data                   # un dict Python, les données nettoyées
# bb.save()                           # LÀ, un vrai objet Book est créé en base et retourné
# bb.instance


from rest_framework import serializers
from demo_function.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','year']



