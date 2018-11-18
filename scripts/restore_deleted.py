from blog.models import Page
from reversion.models import Version

def run():
    versions = Version.objects.get_deleted(Page)
    print(versions)
    index = len(versions)
    reverted = []
    for v in versions.reverse():
        print(v.object_id)
#        if v.object_id not in reverted:
        v.revision.revert()
        p = Page.objects.get(id=v.object_id)
        p.save()
#            reverted.append(v.object_id)
