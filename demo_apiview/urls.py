
from django.urls import path

from demo_apiview.views import BookListCreateView, BookDetailDeletePatchView


urlpatterns = [
        path('books/', BookListCreateView.as_view(), name='demo-apiview-list-create'),
        path('books/<int:pk>', BookDetailDeletePatchView.as_view(), name='demo-apiview-detail-delete-patch'),


        ]
