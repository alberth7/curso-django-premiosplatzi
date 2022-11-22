from importlib.resources import path
from nturl2path import url2pathname
from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/blackpink2022", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# path("<int:question_id>/blackpink", views.detail, name="index"),
'''
urlpatterns = [
    path("", views.Index, name="index"),
    path("<int:question_id>/blackpink2022", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
'''