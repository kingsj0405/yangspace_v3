from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Page(MPTTModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    parent = TreeForeignKey('self',
                            null=True, blank=True,  # Root page is Space
                            related_name='children',
                            db_index=True,
                            on_delete=models.SET_NULL)

    class MPTTMeta:
        order_insertion_by = ['title']
