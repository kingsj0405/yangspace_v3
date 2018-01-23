from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from re import sub


class Page(MPTTModel):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    parent = TreeForeignKey('self',
                            null=True, blank=True,  # Root page is Space
                            related_name='children',
                            db_index=True,
                            on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.url = sub('[^\w\-]+', '', sub('\s+', '-', self.title.lower()))
        super().save(*args, **kwargs)

    class MPTTMeta:
        order_insertion_by = ['title']
