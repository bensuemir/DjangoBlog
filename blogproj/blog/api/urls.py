from django.urls import path
from blog.api import views as api_views

urlpatterns = [
    path('posts/',api_views.PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>', api_views.PostDetailAPIView.as_view(), name='post-detail')
]


"""
urlpatterns = [
    path('posts/',api_views.post_list_create_api_view, name='post-list'),
    path('posts/<int:pk>', api_views.post_detail_api_view, name='post-detay')
]
"""