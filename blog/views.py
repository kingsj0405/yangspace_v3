from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _


def index(request):
    return redirect('/blog')


def main(request):
    return render(request, 'blog/main.html', {
        'title': _('YangSpace') + ' - ' + _('blog'),
    })
