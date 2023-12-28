from django.urls import path
from django.views.generic import DeleteView

from .views import GetPost, GetDetail, CreatePost, UpdatePost, DeletePost, index

urlpatterns = [
    path('', GetPost.as_view(), name='home'),
    path('detail/<int:pk>', GetDetail.as_view(), name='detail'),
    path('create', CreatePost.as_view(), name='create'),
    path('update/<int:pk>', UpdatePost.as_view(), name='update'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete'),
    path('index', index, name='index')
]