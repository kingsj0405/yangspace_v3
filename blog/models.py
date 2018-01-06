from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    parent = models.ForeignKey('self',
                               null=True, blank=True,  # Root page is Space
                               related_name='children',
                               on_delete=models.CASCADE)
