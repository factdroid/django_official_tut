from django.urls import path

from . import views


app_name = 'polls'

urlpatterns = [
    # exqmple /polls/
    path('', views.index, name='index'),
    # exqmple /polls/about
    path('about', views.about, name='about'),
    # exqmple /polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    # exqmple /polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    # exqmple /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
