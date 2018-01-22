from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _

from .constants import *
from .models import Page


def index(request):
    return redirect('/blog/')


def main(request):
    return render(request, 'blog/main.html', {
        'title': _('YangSpace') + ' - ' + _('blog'),
        'pages': Page.objects.all(),
    })


@login_required(login_url='/accounts/login/')
def create(request, parent_url=''):
    if request.method == 'GET':
        page = Page.objects.filter(url=parent_url).first()
        return render(request, 'blog/create.html', {
            'parent_title': DEFAULT_PARENT_PAGE if not page else page.title,
        })
    elif request.method == 'POST':
        # make new page
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_page = Page(title=title, content=content)
        # check parent title and set if needed
        parent_title = request.POST.get('parent_title')
        if parent_title != DEFAULT_PARENT_PAGE:
            parent_page = Page.objects.filter(title=parent_title).first()
            if parent_page:
                new_page.parent = parent_page
        # save new page and redirect to main
        new_page.save()
        return redirect('main')


def read(request, page_url=''):
    if request.method == 'GET':
        page = get_object_or_404(Page, url=page_url)
        return render(request, 'blog/read.html', {
            'title': _('YangSpace') + ' - ' + _('blog') + ' | ' + _(page.title),
            'page': page,
        })


@login_required(login_url='/accounts/login/')
def update(request, parent_url=''):
    return NotImplementedError


@login_required(login_url='/accounts/login/')
def delete(request, parent_url=''):
    return NotImplementedError
