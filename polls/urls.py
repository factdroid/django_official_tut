from django.urls import path

from . import views


app_name = 'polls'

urlpatterns = [
    # exqmple /polls/
    path('', views.IndexView.as_view(), name='index'),
    # exqmple /polls/about
    path('about', views.about, name='about'),
    # exqmple /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # exqmple /polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # exqmple /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
