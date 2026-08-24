
from rest_framework.routers import DefaultRouter
from django.urls import path

from library.views import AuthorViewSet, BookViewSet, create_loan_func

# on creer un objet router, ou lui attribut les views 


router = DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)


urlpatterns = [
        path('loans/create/', create_loan_func, name='loan-create')
        ] + router.urls 



# Les names ? vu que je les choisi pas ?
# se fait tout seul exemple:
# - book-list --> correspond a /library/books/    : GET et POST(creation)
# - book-detail --> correspond a /library/books/{pk} : GET (detail) , PUT, PATCH et DELETE
