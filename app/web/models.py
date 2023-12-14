from datetime import datetime
from typing import TYPE_CHECKING

from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    if TYPE_CHECKING:
        id: int
        name: str
        slug: str
    else:
        id = models.SmallAutoField(primary_key=True)
        name = models.CharField(max_length=32, null=False, blank=False)
        slug = models.SlugField(max_length=32, null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    if TYPE_CHECKING:
        id: int
        title: str
        body: str
        date_created: datetime
        slug: str
        category: Category
    else:
        title = models.CharField(max_length=128, null=False, blank=False)
        body = models.TextField()
        date_created = models.DateTimeField(default=now)
        slug = models.SlugField(max_length=128, null=False, blank=False, unique=True)
        category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title
