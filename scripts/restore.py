from blog.models import Page
from reversion.models import Version

def run():
    pages = Page.objects.all()
    for p in pages:
        versions = Version.objects.get_for_object(p)
        versions[0].revision.revert()
        p.save()
