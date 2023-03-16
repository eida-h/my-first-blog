from django.urls import path
from .views import  PostListView, CreatePostView

app_name = 'knowlight'

urlpatterns = [
    path('',PostListView.as_view(), name='post_list'),
    path('post/', CreatePostView.as_view(), name='post_create')
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
]