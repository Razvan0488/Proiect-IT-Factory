from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('create_book/', views.BookCreate.as_view(), name='book_create'),
    path('update_book/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('delete_book/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
    # path('search_book/<str:book_title>/', views.BookSearch.as_view(), name='title_search'),
    path('search_book/', views.BookSearch.as_view(), name='title_search'),
]