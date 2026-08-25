
from rest_framework.routers import DefaultRouter 

from demo_viewset.views import BookViewSet 

# on cree un router quon rempli avec les champs de la viewset , on attribue le prefixe d'url et on le branche 

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls

# creer auto: 
# GET    /books/          -> list
# POST   /books/          -> create
# GET    /books/{pk}/     -> retrieve
# PUT    /books/{pk}/     -> update
# PATCH  /books/{pk}/     -> partial_update
# DELETE /books/{pk}/     -> destroy

