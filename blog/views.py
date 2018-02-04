from io import BytesIO
from os import path, listdir
from subprocess import run, CalledProcessError
from zipfile import ZipFile

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django_ajax.decorators import ajax
import reversion

from .constants import *
from .models import Page


def index(request):
    return redirect('/blog/')


def main(request):
    return render(request, 'blog/main.html', {
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
        # save new page and redirect to created page
        with reversion.create_revision():
            new_page.save()
            reversion.set_user(request.user)
            reversion.set_comment(_("Create Page"))
        return redirect('read', page_url=new_page.url)


def read(request, page_url=DEFAULT_PARENT_PAGE):
    if page_url == DEFAULT_PARENT_PAGE:
        return redirect('main')
    elif request.method == 'GET':
        page = get_object_or_404(Page, url=page_url)
        return render(request, 'blog/read.html', {
            'page': page,
            'pages': Page.objects.all(),
        })


@login_required(login_url='/accounts/login/')
def update(request, page_url=''):
    if request.method == 'GET':
        page = Page.objects.filter(url=page_url).first()
        return render(request, 'blog/update.html', {
            'page': page,
        })
    elif request.method == 'POST':
        url = request.POST.get('url')
        page = Page.objects.filter(url=url).first()
        # update page
        page.title = request.POST.get('title')
        page.content = request.POST.get('content')
        with reversion.create_revision():
            page.save()
            reversion.set_user(request.user)
            reversion.set_comment(_("Update Page"))
        return redirect('read', page_url=page.url)


@login_required(login_url='/accounts/login/')
def delete(request, page_url=''):
    if request.method == 'GET':
        page = Page.objects.filter(url=page_url).first()
        parent_url = DEFAULT_PARENT_PAGE if not page.parent else page.parent.url
        page.delete()
        return redirect('read', page_url=parent_url)


@login_required(login_url='/accounts/login/')
def download_debug_info(request):
    # Files (local path) to put in the .zip
    dirname = path.join(settings.BASE_DIR, 'data')
    filenames = [path.join(dirname, x) for x in listdir(dirname)]

    # Folder name in ZIP archive which contains the above files
    zip_subdir = "debug_info"
    zip_filename = "%s.zip" % zip_subdir

    # Open ByteIO to grab in-memory ZIP contents
    b = BytesIO()

    # The zip compressor
    zf = ZipFile(b, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = path.split(fpath)
        zip_path = path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(b.getvalue(), content_type="application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp


@login_required(login_url='/accounts/login/')
def server_backup(request):
    try:
        run([settings.BASE_DIR, 'scripts', 'backup.sh'])
        messages.success(request, _('Backup success.'))
    except PermissionError:
        messages.error(request, _('Backup failure. Check process permission.'))
    except CalledProcessError:
        messages.error(request, _('Backup failure. Check debug log for more information.'))
    return redirect('main')


@ajax
def api_page(request):
    if request.method == 'GET':
        page_id = request.GET['page_id']
        page = get_object_or_404(Page, id=page_id)
        return {
            'title': page.title,
            'content': page.content,
        }
