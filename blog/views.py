from django.shortcuts import render, redirect


def index(request):
    return redirect('/blog')


def main(request):
    return render(request, 'main.html')
