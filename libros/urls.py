from django.urls import path

from . import views

app_name = 'libros'
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    
    path("authors/", views.authors, name="authors"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("add_author/", views.add_author, name="add_author"),
    path("edit_author/<int:author_id>/", views.edit_author, name="edit_author"),
    path("delete_author/<int:author_id>/", views.delete_author, name="delete_author"),
    
    path("catalogs/", views.catalogs, name="catalogs"),
    path("catalog/<int:catalog_id>/", views.catalog_detail, name="catalog_detail"),
    path("add_catalog/", views.add_catalog, name="add_catalog"),
    path("edit_catalog/<int:catalog_id>/", views.edit_catalog, name="edit_catalog"),
    path("delete_catalog/<int:catalog_id>/", views.delete_catalog, name="delete_catalog"),
    
    path("books/", views.books, name="books"),
    path("book/<int:book_id>/", views.book_detail, name="book_detail"),
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
    
    path("clients/", views.clients, name="clients"),
    path("client/<int:client_id>/", views.client_detail, name="client_detail"),
    path("add_client/", views.add_client, name="add_client"),
    path("edit_client/<int:client_id>/", views.edit_client, name="edit_client"),
    path("delete_client/<int:client_id>/", views.delete_client, name="delete_client"),
    
     path("compras/", views.compras, name="compras"),
    path('crear_compra/', views.crear_compra, name='crear_compra'),
    path('detalle_compra/<pk>/', views.detalle_compra, name='detalle_compra'),
    path('calcular_total/', views.calcular_total, name='calcular_total'),
]
