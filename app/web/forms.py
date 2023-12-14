from django.forms import *
from .models import Category

__all__ = [
    "CategoryCreateForm",
    "CommentForm",
    "FeedbackForm",
]


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class CommentForm(Form):
    comment = CharField(max_length=1024)


class FeedbackForm(Form):
    message = CharField(max_length=4096)
