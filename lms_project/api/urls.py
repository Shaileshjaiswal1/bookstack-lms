from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book_view, name='edit_book'),
    path('delete_book/<int:delete_book>/', views.delete_book_view, name='delete_book'),
    # path('view_book/', views.view_book, name='view_book'),
    
]