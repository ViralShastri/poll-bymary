from django.urls import path

from . import views
from django.conf.urls import url

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    path('comments/list/', views.commentLists, name='commentLists'),
    path('comments/', views.makeComment, name='makeComment'),
    path('post-comment/', views.postComment, name='postComment'),
    

]