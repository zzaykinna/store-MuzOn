from django.shortcuts import render
from myapp1.models import Worker, Catalog, About


def index_page(request):

    return render(request, 'index.html')

def catalog_page(request):
    all_catalogs = Catalog.objects.all()
    return render(request, 'Catalog.html', context={'data1': all_catalogs})

def about_page(request):
    all_abouts = About.objects.all()
    return render(request, 'About.html', context={'data2': all_abouts})

def sotrud_page(request):
    all_workers = Worker.objects.all()
    return render(request, 'Sotrud.html', context={'data': all_workers})