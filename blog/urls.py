from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    # path('', views.index),
    path('<int:pk>', views.PostDetail.as_view()),
    # path('<int:pk>', views.single_post_page),
    path('category/<str:slug>', views.categories_page),
    path('tag/<str:slug>', views.tags_page),
    path('create_post', views.PostCreate.as_view()),
    path('update_post/<int:pk>', views.PostUpdate.as_view()),
    path('<int:pk>/new_comment', views.new_comment)
]