from django.urls import path
from blogapp import views 

app_name = 'blogapp'

urlpatterns = [
    path('list/',views.PostListView.as_view(),name='post_list'),
    path('create/',views.PostCreateView.as_view(),name='post_new'),
    path('post/detail/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/delete/<int:pk>',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/edit/<int:pk>',views.PostUpdateView.as_view(),name='post_edit'),
    path('add_comment/<int:pk>',views.add_comment_to_post,name='addcomment'),
    path('delete_comment/<int:pk>',views.comment_remove,name='commentdelete'),
    
]