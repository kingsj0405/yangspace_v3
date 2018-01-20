from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _

from .models import Page


def index(request):
    return redirect('/blog/')


def main(request):
    return render(request, 'blog/main.html', {
        'title': _('YangSpace') + ' - ' + _('blog'),
        'pages': Page.objects.all(),
    })


def page(request, page_url=None):
    if request.method == 'GET':
        page = get_object_or_404(Page, url=page_url)
        return render(request, 'blog/page.html', {
            'title': _('YangSpace') + ' - ' + _('blog') + ' | ' + _(page.title),
            'page': page,
        })
