
from rest_framework.routers import DefaultRouter

from library.views import AuthorViewSet, BookViewSet

# on creer un objet router, ou lui attribut les views 

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)

urlpatterns = router.urls 


