from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    url = request.get_full_path()

    if url == '/catalog/':
        phones = Phone.objects.all()
    else:
        sort = request.GET['sort']
        if sort == 'name':
            phones = Phone.objects.all().order_by('name')
        elif sort == 'min_price':
            phones = Phone.objects.all().order_by('price')
        elif sort == 'max_price':
            phones = Phone.objects.all().order_by('-price')
    context = {'phones': phones}
    return render(request, template, context)



def show_product(request, slug):
    phones = Phone.objects.filter(slug=slug)
    template = 'product.html'
    context = {'phones': phones}
    return render(request, template, context)



