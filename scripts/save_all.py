"""
Usage:

python manage.py runscript save_all
"""

from blog.models import Page


def run():
    pages = Page.objects.all()
    for p in pages:
        p.save()
