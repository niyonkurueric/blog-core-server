from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('post_detail/<pk>/', views.post_detail, name='blog-detail'),
    # path('post_edit/<pk>/', views.post_edit, name='blog-post-edit'),
    # path('post_delete/<pk>/', views.post_delete, name='blog-post-delete'),
    # path ('', views.home)
]
