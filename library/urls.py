
from rest_framework.routers import DefaultRouter

from library.views import AuthorViewSet, BookViewSet

# on creer un objet router, ou lui attribut les views 


router = DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)

urlpatterns = router.urls 



# Les names ? vu que je les choisi pas ?
# se fait tout seul exemple:
# - book-list --> correspond a /library/books/    : GET et POST(creation)
# - book-detail --> correspond a /library/books/{pk} : GET (detail) , PUT, PATCH et DELETE
