from django.urls import path
from .views import *

urlpatterns = [
    path("", PostListView.as_view()),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("<slug:slug>/comment/", process_comment, name="post_comment"),
    path("<slug:slug>/feedback/", process_feedback, name="post_feedback"),
]
